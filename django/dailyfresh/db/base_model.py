from django.db import models


class BaseModel(models.Model):
    """一个抽象的模型几类，添加了时间，之后的模型都继承与这个基类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明该类为一个抽象类
        abstract = True
