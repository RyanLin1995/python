from django.db import models
# 设计和表对应的类，模型类
# Create your models here.


# 一类
# 图书类
class BookInfo(models.Model):
    """图书模型类"""
    # 数据库的 ID 由 Django 自动生成
    # ChaField 声明这是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 声明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名让后台管理界面显示为书名
        return self.btitle


# 多类
# 英雄人物类
# 姓名 name
# 性别 gender
# 年龄 age
# 技能 skill
# 定义关系属性 hbook，建立图书类和英雄类之间的一对多关系
class HeroInfo(models.Model):
    """英雄人物模型类"""
    name = models.CharField(max_length=20)
    # BooleanField 声明是布尔类型， default 指定默认值， False 代表男性
    gender = models.BooleanField(default=False)
    # skill
    skill = models.CharField(max_length=128)
    # 建立一对多关系
    # 关系属性对应的表的字段名格式： 关系属性名称_id，如 hbook_id
    hbook = models.ForeignKey(to='BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        # 返回英雄名让后台管理界面显示
        return self.name