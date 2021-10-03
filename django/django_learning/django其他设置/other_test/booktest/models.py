from django.db import models


# Create your models here.


class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称
    atitle = models.CharField(max_length=20, verbose_name='标题')  # verbose_name 参数用于设置该属性在 admin 页面中的显示名称
    # 自关联
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    title.admin_order_field = 'atitle'  # 设置方法返回值在 admin 页面中以 'atitle' 值进行排序
    title.short_description = '地区名称'  # 设置方法返回值在 admin 页面中显示的名字

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle

    parent.admin_order_field = 'atitle'
    parent.short_description = '父级地区'  # 父级地区的名称


class PicTest(models.Model):
    """上传图片"""
    goods_pic = models.ImageField(upload_to='booktest')  # upload_to 参数指图片要上传的目录，该目录相对于 media_root
