from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import users, statistical, specs, images

urlpatterns = [
    re_path(r'^authorizations/$', obtain_jwt_token),
    # --------------数据统计--------------
    # 用户总量统计
    re_path(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
    # 日增用户统计
    re_path(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 日活用户统计
    re_path(r'^statistical/day_active/$', statistical.UserDayActivateView.as_view()),
    # 当天下单用户统计
    re_path(r'^statistical/day_orders/$', statistical.UserDayOrdersCountView.as_view()),
    # 月增用户统计
    re_path(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 日分类商品访问量
    re_path(r'^statistical/goods_day_views/$', statistical.GoodsCountView.as_view()),

    # --------------用户管理--------------
    re_path(r'^users/$', users.UserView.as_view()),

    # --------------规格--------------
    re_path(r'^goods/simple/$', specs.SpecsView.as_view({'get': 'simple'})),

    # --------------图片--------------
    re_path(r'^skus/simple/$', images.ImageView.as_view({'get': 'simple'})),
]

# ------------规格表路由------------
router = DefaultRouter()
router.register('goods/specs', specs.SpecsView, basename='specs')
urlpatterns += router.urls

# ------------图片表路由------------
router = DefaultRouter()
router.register('skus/images', images.ImageView, basename='images')
urlpatterns += router.urls
