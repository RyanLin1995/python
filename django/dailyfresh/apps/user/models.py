from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):
    """用户模型类"""

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class AddressManager(models.Manager):
    """地址模型管理器类"""
    # 自定义模型管理器方法的原因场景：
    # 1. 改变原有的查询方法的默认行为
    # 2. 封装新的方法(增删改查)
    def get_default_address(self, user):
        """获取用户默认收货地址"""
        # self.model: 获取 self 对象所在的模型类，即谁调用它，它就获取谁的模型类
        # 即：Address.objects.get_default_address(user) 中， self.model = Address
        try:
            address = self.get(user=user, is_default=True)  # 这里用 self 而不用 self.model.objects 是因为两者是一样的
        except self.model.DoesNotExist:
            address = None
        return address


class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey('User', verbose_name='所属账户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器对象
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name