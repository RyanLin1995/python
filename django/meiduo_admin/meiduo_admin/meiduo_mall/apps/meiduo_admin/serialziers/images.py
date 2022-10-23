from rest_framework import serializers

from goods.models import SKUImage, SKU


class ImageSerializer(serializers.ModelSerializer):
    """
        图片序列化器
    """

    class Meta:
        model = SKUImage
        fields = '__all__'


class SKUSerializer(serializers.ModelSerializer):
    """
        SKU 序列化器
    """

    class Meta:
        model = SKU
        fields = ('id', 'name')
