from rest_framework.permissions import IsAdminUser
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
