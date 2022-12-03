from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU, GoodsCategory, SPU
from meiduo_admin.serialziers.skus import SKUSerializer, GoodsCategorySerializer, SPUSpecificationSerializer
from meiduo_admin.utils import PageNum


class SKUView(ModelViewSet):
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定查询集
    queryset = SKU.objects.all().order_by('id')
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """
            重写 GenericAPIView 中的方法以满足 user 搜索
        """
        if self.request.query_params.get('keyword') == '':
            return SKU.objects.all().order_by('id')  # 搜索所用商品
        elif self.request.query_params.get('keyword') is None:
            return SKU.objects.all().order_by('id')  # 修改商品时因为没有 keyword 字样，所以要判断 keyword 是否为 None
        else:
            return SKU.objects.filter(name__contains=self.request.query_params.get('keyword')).order_by(
                'id')  # 搜索单一商品，contains 激活模糊查询

    @action(methods=['get'], detail=False)  # 自定义方法自动生成路由
    def categories(self, request):
        """
            获取商品三级分类
        @return:
        """
        data = GoodsCategory.objects.filter(subs__id=None)
        ser = GoodsCategorySerializer(data, many=True)
        return Response(ser.data)

    def specs(self, request, pk):
        """
            获取 spu 商品规格信息
        @param request:
        @param pk: spu 表的 id 值
        @return:
        """
        # 1、 查询 spu 对象
        spu = SPU.objects.get(id=pk)
        # 2、 关联查询 spu 所关联的规格表
        data = spu.specs.all()
        # 3、 序列化返回规格信息
        ser = SPUSpecificationSerializer(data, many=True)
        return Response(ser.data)
