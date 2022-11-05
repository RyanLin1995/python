from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from celery_tasks.static_file.tasks import get_detail_html
from goods.models import SKUImage, SKU
from meiduo_mall.settings import dev


class ImageSerializer(serializers.ModelSerializer):
    """
        图片序列化器
    """

    class Meta:
        model = SKUImage
        fields = '__all__'

    def create(self, validated_data):
        # 1. 建立 FDFS 客户端
        client = Fdfs_client(dev.FDFS_PATH)
        # self.context['request'] 可以获取 request 对象
        file = self.context['request'].FILES.get('image')  # 获取文件
        # 2. 上传图片
        res = client.upload_by_buffer(file.read())  # file 是文件对象，可以直接 read
        # 3. 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError(({'error': '图片上传失败'}))
        # 4. 保存图片表
        img = SKUImage.objects.create(sku=validated_data['sku'], image=res['Remote file_id'])

        # 5. 异步生成对应 sku 详情页面
        get_detail_html.delay(img.sku.id)

        return img

    def update(self, instance, validated_data):
        # 1. 建立 FDFS 客户端
        client = Fdfs_client(dev.FDFS_PATH)
        # self.context['request'] 可以获取 request 对象
        file = self.context['request'].FILES.get('image')  # 获取文件
        # 2. 上传图片
        res = client.upload_by_buffer(file.read())  # file 是文件对象，可以直接 read
        # 3. 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError(({'error': '图片上传失败'}))
        # 4. 更新图片表
        instance.image = res['Remote file_id']
        instance.save()

        # 5. 异步生成对应 sku 详情页面
        get_detail_html.delay(instance.sku.id)

        return instance


class SKUSerializer(serializers.ModelSerializer):
    """
        SKU 序列化器
    """

    class Meta:
        model = SKU
        fields = ('id', 'name')
