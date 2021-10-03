from django.contrib import admin
from booktest import models


# Register your models here.
class AreaStackedInline(admin.StackedInline):
    """以块形式显示多类"""
    # 写多类的名字
    model = models.AreaInfo
    extra = 2


class AreaTabularInline(admin.TabularInline):
    """以表形式显示多类"""
    model = models.AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    """模型管理类"""
    # 指定每页显示10条数据
    list_per_page = 10
    # 指定显示内容，其中可以写模型类的属性和方法
    list_display = ['id', 'atitle', 'title', 'parent']
    # 显示下列表框
    actions_on_bottom = True
    actions_on_top = False
    # 设置右侧过滤栏
    list_filter = ['atitle']
    # 列表页上方显示搜索框
    search_fields = ['atitle', 'aParent__atitle']  # 如果搜索字段是外键时，需要用 外键__关联表名称 加上
    # 调换编辑页面中显示字段的顺序
    # fields = ['aParent', 'atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']}),
    )
    # 在一类中嵌入多类
    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]


admin.site.register(models.AreaInfo, AreaInfoAdmin)
admin.site.register(models.PicTest)
