from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serialziers.group import GroupSerializers
from meiduo_admin.serialziers.permission import PermissionSerializer
from meiduo_admin.utils import PageNum


class GroupView(ModelViewSet):
    """
        用户组视图
    """
    serializer_class = GroupSerializers
    queryset = Group.objects.all().order_by('id')
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    # @action(methods=['get'], detail=False)  # methods 指定请求方法，detail指定生成的路径是否需要正则匹配
    def simple(self, request):
        """
            获取权限数据
        @param request:
        @return:
        """
        # 1、查询权限表
        data = Permission.objects.all().order_by('id')
        # 2、返回权限数据
        ser = PermissionSerializer(data, many=True)
        # 3、返回
        return Response(ser.data)
