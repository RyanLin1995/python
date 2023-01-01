from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializers(serializers.ModelSerializer):
    """
        Group 的序列化器
    """

    class Meta:
        model = Group
        fields = '__all__'
