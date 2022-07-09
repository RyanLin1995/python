from django.db import models

# Create your models here.


# Create your models here.
class BookInfoManager(models.Manager):
    """图书模型管理器类"""

    # 1. 改变查询的结果集
    def all(self):
        # 1. 调用父类 all 方法获取所有数据
        books = super().all()  # 返回的是查询机 queryset
        # 2. 对数据进行过滤
        books = books.filter(isdelete=0)
        # 3. 返回结果
        return books

    # 2. 封装函数：操作模型类对应的数据表（增删改查）
    def create_book(self, btitle, bpub_date):
        # book = BookInfo()
        model_class = self.model  # 获取 self 所在的模型类
        book = model_class()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book

    # 其实 models.Manager 类已经封装了一个 create 函数，通过关键字参数传参
    # BookInfo.objects.create(btitle='test3', bpub_date='1990-10-10')


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

    # 自定义 manager 类对象（管理器对象），通常不直接创建
    # book = models.Manager()

    # 自定义一个 BookInfoManager 类对象
    # objects = BookInfoManager()

    def __str__(self):
        return self.btitle

    class Meta:
        """元选项，用于指定模型类的表的名称，格式固定"""
        db_table = 'bookinfo'


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

    def __str__(self):
        return self.name