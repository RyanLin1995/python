from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

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
            try:
                sku = GoodsSKU.objects.get(id=sku_id)
            except Exception as e:
                return JsonResponse({'res': 0, 'errmsg': '商品不存在'})

            # 从 redis 中获取用户所要购买商品的数量
            count = conn.hget(cart_key, sku_id)

            # 向 df_order_goods 添加记录
            OrderGoods.objects.create(order=order,
                                      sku=sku,
                                      count=count,
                                      price=sku.price)

            # 更新商品库存和销量
            sku.stock -= int(count)
            sku.sales += int(count)
            sku.save()

            # 累加计算订单总数量和总金额
            amount = sku.price * int(count)
            total_count += int(count)
            total_price += amount

        # 更新 df_order_info 总数量和总金额
        order.total_count = total_count
        order.total_price = total_price
        order.save()

        # 清空用户购物车中对应的记录
        conn.hdel(cart_key, *sku_ids)  # 对 sku_ids 进行拆包

        # 返回应答
        return JsonResponse({'res': 1, 'errmsg': '创建成功'})
