from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serialziers.images import ImageSerializer, SKUSerializer
from meiduo_admin.utils import PageNum


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

    # 为什么在序列化器中定义了 create 方法后下边的可以注释掉，是因为序列化器中已经重写了 create 方法，且在一开始指定了序列化器，
    # 那么序列化器的 create 方法则为实际业务操作的保存方法，下面的代码跟它是重复了
    # def create(self, request, *args, **kwargs):
    #     """
    #         改写 Create 方法
    #     @param request:
    #     @param args:
    #     @param kwargs:
    #     @return:
    #     """
    #     # 1. 获取前端数据
    #     data = request.data
    #     # 2. 验证数据
    #     ser = self.get_serializer(data=data)
    #     ser.is_valid()
    #     # 3. 保存
    #     ser.save()
    #     # 4. 返回保存后的图片数据
    #     return Response(ser.data, status=201)
