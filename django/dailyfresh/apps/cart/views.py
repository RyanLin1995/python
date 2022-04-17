from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django_redis import get_redis_connection
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.goods.models import GoodsSKU


# 添加商品到购物车的请求方式
# 1. post 涉及到数据的修改（增、该、更）用 post
# 2. get 涉及到数据的查询（查）用 get
# 3. delete 涉及到数据的删除（删）用 delete
# 4. url 传参也可以


# Create your views here.
class CartAddView(View):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})
        # 这里不使用 LoginRequiredMixin 的原因是前端使用了 ajax 发起请求。而 ajax 发起的请求都是在后台，不会显示在浏览器上，
        # 所以如果使用 LoginRequiredMixin，虽然后返回并访问了登录页面，但是不会显示在浏览器上。

        # 接收数据
        sku_id = request.POST.get('sku_id')
        num = request.POST.get('num')

        # 数据校验
        if not all([sku_id, num]):
            return JsonResponse({'res': 0, 'errmsg': '数据不完整'})
        # 校验添加的商品数量
        try:
            num = int(num)
        except Exception as e:
            return JsonResponse({'res': 0, 'errmsg': '商品数目出错'})
        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '商品不存在'})

        # 业务处理--添加购物车记录
        # 先检查用户在数据库中是否有数值
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'
        cart_count = conn.hget(cart_key, sku_id)
        if cart_count:
            # 累加购物车中商品的数量
            num += int(cart_count)
        # 校验商品的库存
        if num > sku.stock:
            return JsonResponse({'res': 0, 'errmsg': '商品库存不足'})
        # 设置hash中sku_id对应的值
        conn.hset(cart_key, sku_id, num)

        # 计算用户购物车中商品总数
        total_num = conn.hlen(cart_key)

        # 返回应答
        return JsonResponse({'res': 1, 'message': '添加成功', 'total_num': total_num})


class CartInfoView(View, LoginRequiredMixin):
    """购物车页面显示"""

    def get(self, request):
        user = request.user
        # 获取用户购物车中商品的信息
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'
        cart_dict = conn.hgetall(cart_key)  # hgetall 返回的是一个字典
        skus = []
        total_num = 0
        total_price = 0
        for sku_id, num in cart_dict.items():
            # 根据商品 ID 获取商品的信息
            sku = GoodsSKU.objects.get(id=sku_id)
            # 计算商品的小计
            amount = sku.price * int(num)
            # 动态给 sku 对象增加一个属性来保存商品的小计
            sku.amount = amount
            # 给 sku 动态增加一个属性来保存购物车中商品的数目
            sku.num = int(num)
            # 添加到列表中
            skus.append(sku)
            # 累加商品的总数目和总价格
            total_num += int(num)
            total_price += amount

        # 组织模板上下文
        context = {'total_num': total_num,
                   'total_price': total_price,
                   'skus': skus}

        return render(request, 'cart.html', context)


# 更新购物车记录
# 采用 ajax post 请求，传递商品id(sku_id)跟商品数量
class CartUpdateView(View):
    def post(self, request):
        """购物车记录更新"""
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        num = request.POST.get('num')

        # 数据校验
        if not all([sku_id, num]):
            return JsonResponse({'res': 0, 'errmsg': '数据不完整'})
        # 校验添加的商品数量
        try:
            num = int(num)
        except Exception as e:
            return JsonResponse({'res': 0, 'errmsg': '商品数目出错'})
        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '商品不存在'})

        # 业务处理：更新购物车记录
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'

        # 校验商品库存
        if num > sku.stock:
            return JsonResponse({'res': 0, 'errmsg': '商品库存不足'})

        # 更新
        conn.hset(cart_key, sku_id, num)

        # 统计用户购物车中商品的总件数
        total_count = 0
        vals = conn.hvals(cart_key)  # hvals 将 hash 中的值作为列表返回
        for val in vals:
            total_count += int(val)

        # 返回应答
        return JsonResponse({'res': 1, 'errmsg': '更新成功', 'total_count': total_count})


# 删除购物车记录
# 采用 ajax post 请求，传递商品id(sku_id)
class CartDeleteView(View):
    def post(self, request):
        """购物车记录更新"""
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')

        # 数据校验
        if not sku_id:
            return JsonResponse({'res': 0, 'errmsg': '数据不完整'})
        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 0, 'errmsg': '商品不存在'})

        # 业务处理：删除购物车记录
        conn = get_redis_connection('default')
        cart_key = f"cart_{user.id}"
        conn.hdel(cart_key, sku_id)

        # 统计用户购物车中商品的总件数
        total_count = 0
        vals = conn.hvals(cart_key)  # hvals 将 hash 中的值作为列表返回
        for val in vals:
            total_count += int(val)

        # 返回应答
        return JsonResponse({'res': 1, 'errmsg': '删除成功', 'total_count': total_count})

