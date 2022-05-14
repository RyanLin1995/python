from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db import transaction

from apps.goods.models import GoodsSKU
from apps.user.models import Address
from apps.order.models import OrderInfo, OrderGoods

from django_redis import get_redis_connection


# Create your views here.

# /order/place
class OrderPlaceView(LoginRequiredMixin, View):
    """提交订单页面显示"""

    def post(self, request):
        # 获取登录的用户
        user = request.user
        # 获取参数 sku_ids
        sku_ids = request.POST.getlist('sku_ids')  # sku_ids 为自己在页面设置的 name
        # 为什么只传递 sku_ids，是因为前端的数据用户都是可以修改的，不可信。通过 sku_ids 可以直接在数据库中获取所有信息，所以只需传递 sku_id 即可

        # 校验参数
        if not sku_ids:
            # 跳转到购物车页面
            return redirect(reverse('cart:show'))

        conn = get_redis_connection('default')
        cart_key = f"cart_{user.id}"

        skus = []
        total_count = 0
        total_price = 0
        # 遍历 sku_ids 获取用户购买的商品信息
        for sku_id in sku_ids:
            # 获取商品信息
            sku = GoodsSKU.objects.get(id=sku_id)
            # 获取用户购买的商品数量
            count = conn.hget(cart_key, sku_id)
            # 计算商品小计
            amount = sku.price * int(count)
            # 动态给 sku 增加属性，保存订单商品的数目和小计
            sku.count = int(count)
            sku.amount = amount
            # 追加 sku 到订单商品列表
            skus.append(sku)
            # 计算商品的总数目和总价格
            total_count += int(count)
            total_price += amount

        # 运费：实际开发的时候，属于一个专门计算运费的子系统
        transit_price = 10

        # 实付款
        total_pay = total_price + transit_price

        # 获取用户的收件地址
        addrs = Address.objects.filter(user=user)

        # 组织上下文
        sku_ids = ','.join(sku_ids)  # sku_ids 为自己在页面设置的 name
        context = {
            'skus': skus,
            'total_count': total_count,
            'total_price': total_price,
            'transit_price': transit_price,
            'total_pay': total_pay,
            'addrs': addrs,
            'sku_ids': sku_ids,
        }

        # 使用模板
        return render(request, 'place_order.html', context)


# 前端传入的参数：地址id(addr_id) 支付方式(pay_method) 用户要购买的商品id字符串(sku_ids)
class OrderCommitView(View):
    @transaction.atomic()  # Django 启用 MySQL 事务的装饰器
    def post(self, request):
        # 判断用户是否登录
        user = request.user

        if not user.is_authenticated:
            # 用户为登录
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        # 获取参数
        addr_id = request.POST.get('addr_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')

        # 校验参数
        if not all([addr_id, pay_method, sku_ids]):
            return JsonResponse({'res': 0, 'errmsg': '参数不完整'})

        # 校验支付方式
        if pay_method not in OrderInfo.PAY_METHODS.keys():
            return JsonResponse({'res': 0, 'errmsg': '非法的支付方式'})

        # 校验地址
        try:
            addr = Address.objects.get(id=addr_id)
        except Address.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '地址非法'})

        # 创建订单核心业务
        # 订单信息表：df_order_info-->用户每下一个订单就要向这个表添加一条记录
        # 订单商品表：df_order_goods-->用户订单中有几个商品就要向这个表加入几条记录
        # 组织参数
        # order_id 是我们自己设计的，格式为：日期时间+用户id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)
        # 运费
        transit_price = 10
        # 总数目和总金额
        total_count = 0
        total_price = 0

        # 设置 MySQL 事务保存点
        save_id = transaction.savepoint()
        try:
            # 向 df_order_info 表中插入一条记录（因为 df_order_goods 的外键来源于这个表）
            order = OrderInfo.objects.create(order_id=order_id,
                                             user=user,
                                             addr=addr,
                                             pay_method=pay_method,
                                             total_price=total_price,
                                             total_count=total_count,
                                             transit_price=transit_price)
            # 用户订单中有几个商品就要向 df_order_goods 加入几条记录
            conn = get_redis_connection('default')
            cart_key = f"cart_{user.id}"
            for sku_id in sku_ids.split(","):
                # 获取商品的信息
                for i in range(3):  # 循环3次以解决乐观锁库存存在还报错的情况
                    try:
                        sku = GoodsSKU.objects.get(id=sku_id)
                        # sku = GoodsSKU.objects.select_for_update(id=sku_id)  # select_for_update 启用悲观锁，完整 SQL 语句为
                        # select * from df_goods_sku where id=sku_id for update;
                    except Exception as e:
                        transaction.savepoint_rollback(save_id)  # 回滚事务
                        return JsonResponse({'res': 0, 'errmsg': '商品不存在'})

                    # 从 redis 中获取用户所要购买商品的数量
                    count = conn.hget(cart_key, sku_id)

                    # 判断商品的库存
                    if int(count) > sku.stock:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 0, 'errmsg': '库存不足'})

                    # 悲观锁打开以下注释
                    # 向 df_order_goods 添加记录
                    # OrderGoods.objects.create(order=order,
                    #                           sku=sku,
                    #                           count=count,
                    #                           price=sku.price)
                    # 更新商品库存和销量
                    # sku.stock -= int(count)
                    # sku.sales += int(count)
                    # sku.save()

                    # 乐观锁的实现
                    # 其中由于 MySQL 事务隔离级别默认为 Repeatable Read（可重读），会导致幻读的问题，1.0版本的 Django 需要手动改变 MySQL
                    # 事务隔离级别。但是2.0版本 Django 已经不需要
                    orgin_stock = sku.stock
                    new_stock = orgin_stock - int(count)
                    new_sales = orgin_stock + int(count)
                    # 返回的是受影响的行数，以下代码等价于
                    # update df_goods_sku set stock=new_stock, sales=new_sales where id=sku_id and stock = orgin_stock;
                    res = GoodsSKU.objects.filter(id=sku_id, stock=orgin_stock).update(stock=new_stock, sales=new_sales)
                    if res == 0:
                        # 更新失败
                        if i == 2:
                            transaction.savepoint_rollback(save_id)
                            return JsonResponse({'res': 0, 'errmsg': '下单失败'})
                        continue
                    # 向 df_order_goods 添加记录
                    OrderGoods.objects.create(order=order,
                                              sku=sku,
                                              count=count,
                                              price=sku.price)

                    # 累加计算订单总数量和总金额（悲观锁下以下代码往前缩进1）
                    amount = sku.price * int(count)
                    total_count += int(count)
                    total_price += amount

                    # 如果乐观锁更新成功跳出循环
                    break

            # 更新 df_order_info 总数量和总金额
            order.total_count = total_count
            order.total_price = total_price
            order.save()
        except Exception as e:  # 将所有 MySQL 操作放在事务中，如果错误就回滚，否则就提交事务
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'res': 0, "errmsg": '下单失败'})

        # 提交事务
        transaction.savepoint_commit(save_id)

        # 清空用户购物车中对应的记录
        conn.hdel(cart_key, *sku_ids)  # 对 sku_ids 进行拆包

        # 返回应答
        return JsonResponse({'res': 1, 'errmsg': '创建成功'})


class OrderPayView(View):
    """订单支付"""

    def post(self, request):
        # 用户是否登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        # 接收参数
        order_id = request.POST.get('order_id')

        # 校验参数
        if not order_id:
            return JsonResponse({'res': 0, 'errmsg': '无效的订单ID'})

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          pay_method=3,
                                          order_status=1)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '订单错误'})

        # 调用支付宝接口
        # 跳过，因为个人没办法调用支付宝api

        # 返回应答
        pay_url = 'http://127.0.0.1:8000/index'
        return JsonResponse({'res': 1, 'pay_url': pay_url})


# ajax post
# 前端传递的参数:订单id(order_id)
# /order/check
class CheckPayView(View):
    """查看订单支付的结果"""

    def post(self, request):
        """查询支付结果"""
        # 用户是否登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        # 接收参数
        order_id = request.POST.get('order_id')

        # 校验参数
        if not order_id:
            return JsonResponse({'res': 0, 'errmsg': '无效的订单id'})

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          pay_method=3,
                                          order_status=1)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '订单错误'})

        # 业务处理:使用python sdk调用支付宝的支付接口
        # 初始化
        # 调用支付宝的交易查询接口
        order.order_status = 4  # 待评价
        order.save()
        return JsonResponse({'res': 1, 'message': '支付成功'})


class CommentView(LoginRequiredMixin, View):
    """订单评论"""

    def get(self, request, order_id):
        """提供评论页面"""
        user = request.user

        # 校验数据
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse("user:order"))

        # 根据订单的状态获取订单的状态标题
        order.status_name = OrderInfo.ORDER_STATUS[order.order_status]

        # 获取订单商品信息
        order_skus = OrderGoods.objects.filter(order_id=order_id)
        for order_sku in order_skus:
            # 计算商品的小计
            amount = order_sku.count * order_sku.price
            # 动态给order_sku增加属性amount,保存商品小计
            order_sku.amount = amount
        # 动态给order增加属性order_skus, 保存订单商品信息
        order.order_skus = order_skus

        # 使用模板
        return render(request, "order_comment.html", {"order": order})

    def post(self, request, order_id):
        """处理评论内容"""
        user = request.user
        # 校验数据
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse("user:order"))

        # 获取评论条数
        total_count = request.POST.get("total_count")
        total_count = int(total_count)

        # 循环获取订单中商品的评论内容
        for i in range(1, total_count + 1):
            # 获取评论的商品的id
            sku_id = request.POST.get(f"sku_{i}")  # sku_1 sku_2
            # 获取评论的商品的内容
            content = request.POST.get(f'content_{i}', '')  # cotent_1 content_2 content_3
            try:
                order_goods = OrderGoods.objects.get(order=order, sku_id=sku_id)
            except OrderGoods.DoesNotExist:
                continue

            order_goods.comment = content
            order_goods.save()

        order.order_status = 5  # 已完成
        order.save()

        return redirect(reverse("user:order", kwargs={"page": 1}))
