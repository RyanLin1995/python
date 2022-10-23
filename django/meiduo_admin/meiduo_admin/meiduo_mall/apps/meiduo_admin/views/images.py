from fdfs_client.client import Fdfs_client
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serialziers.images import ImageSerializer, SKUSerializer
from meiduo_admin.utils import PageNum
from settings import dev


class ImageView(ModelViewSet):
    queryset = SKUImage.objects.all().order_by('id')
    serializer_class = ImageSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def simple(self, request):
        """
            获取 sku 商品信息
        @param request:
        @return:
        """
        skus = SKU.objects.all().order_by('id')
        ser = SKUSerializer(skus, many=True)

        return Response(ser.data)

    def create(self, request, *args, **kwargs):
        """
            改写 Create 方法
        @param request:
        @param args:
        @param kwargs:
        @return:
        """
        # 1. 获取前端数据
        data = request.data
        # 2. 验证数据
        ser = self.get_serializer(data=data)
        ser.is_valid()
        # 3. 建立 FDFS 客户端
        client = Fdfs_client(dev.FDFS_PATH)
        file = request.FILES.get('image')  # 获取文件
        # 4. 上传图片
        res = client.upload_by_buffer(file.read())  # file 是文件对象，可以直接 read
        # 5. 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response({'error': '图片上传失败'})
        # 6. 保存图片表
        img = SKUImage.objects.create(sku=ser.validated_data['sku'], image=res['Remote file_id'])
        # 7. 返回保存后的图片数据
        return Response({
            'id': img.id,
            'sku': img.sku_id,
            'image': img.image.url
        }, status=201)
