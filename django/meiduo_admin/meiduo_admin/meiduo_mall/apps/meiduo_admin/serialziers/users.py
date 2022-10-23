from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        用户序列化器
    """

    def create(self, validated_data):
        """
            重写父类方法，为密码加密
        @param validated_data:  序列化器验证后的数据
        """
        # 方法一：
        # user = super().create(validated_data)
        # user.set_password(validated_data['password'])  # 加密密码
        # user.save()
        # 方法二：
        user = User.objects.create_user(**validated_data)  # create_user 创建用户的时候自动加密密码
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'password')  # id 字段默认为 read only
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
            },
            'username': {
                'max_length': 20,
                'min_length': 5,
            }
        }
