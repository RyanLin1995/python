from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serialziers.admin import AdminSerializers
from meiduo_admin.serialziers.group import GroupSerializers
from meiduo_admin.utils import PageNum
from users.models import User


class AdminView(ModelViewSet):
    """
        管理员视图
    """
    serializer_class = AdminSerializers
    queryset = User.objects.filter(is_staff=True)
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def simple(self, request):
        """
            查询分组信息
        @param request:
        @return:
        """
        # 1、查询分组表
        data = Group.objects.all().order_by('id')
        # 2、返回分组数据
        ser = GroupSerializers(data, many=True)
        # 3、返回
        return Response(ser.data)
