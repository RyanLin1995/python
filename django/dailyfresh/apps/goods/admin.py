from django.contrib import admin
from django.core.cache import cache

from apps.goods.models import *


# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    """
    基础模型管理类
    """

    def save_model(self, request, obj, form, change):
        """新增或更新表中的数据时调用"""
        super().save_model(request, obj, form, change)

        # 发出任务，让celery worker重新生成静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页缓存数据，使首页缓存重新生成
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """删除表中的数据时调用"""
        super().delete_model(request, obj)

        # 发出任务，让celery worker重新生成静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页缓存数据，使首页缓存重新生成
        cache.delete('index_page_data')


class GoodsTypeAdmin(BaseModelAdmin):
    """商品类型模型管理类"""
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    """首页轮播商品展示模型管理类"""
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    """首页轮播商品展示模型管理类"""
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    """首页促销活动模型管理类"""
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
