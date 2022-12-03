from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods


class SKUSerializer(serializers.ModelSerializer):
    """
        订单商品序列化器
    """

    class Meta:
        model = SKU
        fields = ('name', 'default_image')


class OrderGoodsSerializer(serializers.ModelSerializer):
    """
        订单商品序列化器
    """
    sku = SKUSerializer()

    class Meta:
        model = OrderGoods
        fields = ('count', 'price', 'sku')


class OrderSerializer(serializers.ModelSerializer):
    """
        订单序列化器
    """
    skus = OrderGoodsSerializer(many=True)  # 为什么只需要这里设置 many 是因为这是一个嵌套返回，在 order 中已经嵌套了 sku 的返回值

    class Meta:
        model = OrderInfo
        fields = '__all__'
