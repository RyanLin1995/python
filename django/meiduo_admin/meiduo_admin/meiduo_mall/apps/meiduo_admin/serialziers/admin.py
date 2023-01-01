from rest_framework import serializers

from users.models import User


class AdminSerializers(serializers.ModelSerializer):
    """
        管理员序列化器
    """

    class Meta:
        model = User
        fields = '__all__'
        # 给字段增加额外参数
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # 重写父类保存数据库的方法，因为其不满足需求
    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_staff = True
        user.set_password(validated_data['password'])  # 密码加密过程
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super(AdminSerializers, self).update(instance, validated_data)
        user.set_password(validated_data['password'])  # 密码加密过程
        user.save()

        return user
