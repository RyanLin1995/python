from django.db import models


# Create your models here.
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

    def __str__(self):
        return self.btitle

    class Meta:
        """元选项，用于指定模型类的表的名称，格式固定"""
        db_table = 'bookinfo'