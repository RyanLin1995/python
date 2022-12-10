from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serialziers.orders import OrderSerializer
from meiduo_admin.utils import PageNum
from orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):
    """

    """
    queryset = OrderInfo.objects.all().order_by('order_id')
    serializer_class = OrderSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """
            重写 GenericAPIView 中的方法以满足 order 搜索
        """
        if self.request.query_params.get('keyword') == '':
            return OrderInfo.objects.all().order_by('order_id')  # 搜索所用商品
        elif self.request.query_params.get('keyword') is None:
            return OrderInfo.objects.all().order_by('order_id')  # 修改商品时因为没有 keyword 字样，所以要判断 keyword 是否为 None
        else:
            return OrderInfo.objects.filter(order_id__contains=self.request.query_params.get('keyword')).order_by(
                'order_id')  # 搜索单一商品，contains 激活模糊查询

    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        """
            修改订单状态
        @param request:
        @param pk: 订单编号
        @return:
        """

        # 1、查询要修改的订单对象
        try:
            order = OrderInfo.objects.get(order_id=pk)
        except Exception as e:
            return Response({'error': '订单编号错误'})
        # 2、修改订单状态
        # 获取订单状态
        status = request.data.get('status')
        if status is None:
            return Response({'error': '缺少订单状态'})
        order.status = status
        order.save()
        # 3、返回修改信息
        return Response({
            'order_id': pk,
            'status': status
        })
