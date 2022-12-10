from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serialziers.permission import PermissionSerializer
from meiduo_admin.utils import PageNum


class PermissionView(ModelViewSet):
    """
        权限视图
    """
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    pagination_class = PageNum
    permission_classes = [IsAdminUser]
