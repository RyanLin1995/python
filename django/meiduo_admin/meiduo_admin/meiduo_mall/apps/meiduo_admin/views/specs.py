from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification, SPU
from meiduo_admin.serialziers.specs import SpecsSerializer, SPUSerializer
from meiduo_admin.utils import PageNum


class SpecsView(ModelViewSet):
    """
        商品规格的增删改查
    """
    # 指定查询集
    queryset = SPUSpecification.objects.all().order_by('id')
    serializer_class = SpecsSerializer
    pagination_class = PageNum

    def simple(self, request):
        """
            获取规格所关联的SPU商品信息
        @param request:
        @return:
        """
        spus = SPU.objects.all()
        ser = SPUSerializer(spus, many=True)

        return Response(ser.data)
