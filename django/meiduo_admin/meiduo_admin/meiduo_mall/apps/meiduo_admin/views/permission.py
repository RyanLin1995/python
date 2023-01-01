from django.contrib.auth.models import Permission, ContentType
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serialziers.permission import PermissionSerializer, ContentTypeSerializer
from meiduo_admin.utils import PageNum


class PermissionView(ModelViewSet):
    """
        权限视图
    """
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all().order_by('id')
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    # 父类中缺少权限类型表的操作，需要自己封装方法
    def content_type(self, request):
        """
            获取权限类型
        @param request:
        @return:
        """
        # 1、获取权限类型所有数据
        data = ContentType.objects.all().order_by('id')
        # 2、序列化返回权限类型
        ser = ContentTypeSerializer(data, many=True)
        # 3、序列化返回
        return Response(ser.data)
