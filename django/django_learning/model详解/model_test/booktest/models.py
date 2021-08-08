from django.db import models


# Create your models here.
# 一类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 软删除标记，即做删除时不真正删除，只是在数据库中不显示
    isdelete = models.BooleanField(default=False)


# 多类
class HeroInfo(models.Model):
    """英雄人物模型类"""
    # 英雄名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 技能
    skill = models.CharField(max_length=200)
    # 关系属性
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # 软删除标记，即做删除时不真正删除，只是在数据库中不显示
    isdelete = models.BooleanField(default=False)
