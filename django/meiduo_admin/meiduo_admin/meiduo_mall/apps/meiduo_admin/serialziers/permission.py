from django.contrib.auth.models import Permission, ContentType
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """
        权限类型序列化器
    """
    name = serializers.CharField(read_only=True)

    class Meta:
        model = ContentType
        fields = '__all__'
