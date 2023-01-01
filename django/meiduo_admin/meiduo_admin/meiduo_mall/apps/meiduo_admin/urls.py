from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import users, statistical, specs, images, skus, orders, permission, group, admin

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

    # --------------sku路由--------------
    re_path(r'^goods/(?P<pk>\d+)/specs/$', skus.SKUView.as_view({'get': 'specs'})),

    # --------------权限类型路由--------------
    re_path(r'^permission/content_types/$', permission.PermissionView.as_view({'get': 'content_type'})),

    # --------------用户获取权限路由--------------
    re_path(r'^permission/simple/$', group.GroupView.as_view({'get': 'simple'})),

    # --------------用户组路由--------------
    re_path(r'^permission/groups/simple/$', admin.AdminView.as_view({'get': 'simple'})),
]
router = DefaultRouter()
# ------------规格表路由------------
router.register('goods/specs', specs.SpecsView, basename='specs')
urlpatterns += router.urls

# ------------图片表路由------------
router.register('skus/images', images.ImageView, basename='images')
urlpatterns += router.urls

# ------------SKU表路由------------
router.register('skus', skus.SKUView, basename='skus')
urlpatterns += router.urls

# ------------订单路由------------
router.register('orders', orders.OrderView, basename='orders')
urlpatterns += router.urls

# ------------权限路由------------
router.register('permission/perms', permission.PermissionView, basename='perms')
urlpatterns += router.urls

# ------------用户组路由------------
router.register('permission/groups', group.GroupView, basename='groups')
urlpatterns += router.urls

# ------------管理员路由------------
router.register('permission/admins', admin.AdminView, basename='admin')
urlpatterns += router.urls
