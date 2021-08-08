from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


# 后台管理相关文件
# Register your models here.
# 自定义一个模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    """英雄人物模型管理类"""
    list_display = ['id', 'name', 'skill']


# 注册模型类
# 注意注册只能注册一次，注册多次会报错
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
