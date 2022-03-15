from django.shortcuts import render
from django.views.generic import View
from django.core.cache import cache

from apps.goods.models import *
from django_redis import get_redis_connection


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
class IndexView(View):
    def get(self, request):

        # 尝试获取缓存数据
        context = cache.get('index_page_data')

        if context is None:  # 如果缓存中没有数据，则进行数据库查询
            print('没有缓存')
            # 获取商品的种类信息
            types = GoodsType.objects.all()

            # 获取首页轮播商品信息
            goods_banners = IndexGoodsBanner.objects.all().order_by('index')  # 根据index排序，数字小的排在前边

            # 获取首页促销活动信息
            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

            # 获取首页分类商品展示信息
            for type in types:
                # 获取 type 种类首页分类商品的图片展示信息
                image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
                # 获取 type 种类首页分类商品的文字展示信息
                title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

                # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息，因为 Python 是可以动态添加属性的，所以这里可以直接给 type 增加属性
                type.image_banners = image_banners
                type.title_banners = title_banners

            # 组织模板上下文
            context = {'types': types, 'goods_banners': goods_banners, 'promotion_banners': promotion_banners}

            # 设置缓存
            cache.set('index_page_data', context, 3600)  # set 需要传入三个参数，第一个参数是缓存的键，第二个是需要缓存的值，第三个参数是缓存的时间
            print('设置缓存')

        # 获取购物车商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            r = get_redis_connection('default')
            cart_key = f'cart_{user.id}'
            cart_count = r.hlen(cart_key)

        context.update(cart_count=cart_count)

        # 返回模板
        return render(request, 'index.html', context=context)