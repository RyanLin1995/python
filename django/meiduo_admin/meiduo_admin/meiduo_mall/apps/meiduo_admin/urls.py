from django.urls import re_path
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_mall.apps.meiduo_admin.views.statistical import *

urlpatterns = [
    re_path(r'^authorizations/$', obtain_jwt_token),
    # --------------数据统计--------------
    # 用户总量统计
    re_path(r'^statistical/total_count/$', UserCountView.as_view()),
    # 日增用户统计
    re_path(r'^statistical/day_increment/$', UserDayCountView.as_view()),
    # 日活用户统计
    re_path(r'^statistical/day_active/$', UserDayActivateView.as_view()),
    # 当天下单用户统计
    re_path(r'^statistical/day_orders/$', UserDayOrdersCountView.as_view()),
]
