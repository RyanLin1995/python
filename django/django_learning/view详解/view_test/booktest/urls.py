from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('index/', views.index),
    # re_path(r'showarg(\d+)', views.show_args),  # 位置参数捕获 url 参数
    re_path(r'showarg(?P<num>\d+)', views.show_args),  # 关键字参数捕获 url 参数，url 中的组名必须与 views 中的关键字一致
    path('login/', views.login),
    re_path(r'login_check', views.login_check),
    path('ajax_test', views.ajax_test),  # 显示 ajax 页面
    path('ajax_handle', views.ajax_handle),  # 显示 ajax 处理
    path('login_ajax/', views.login_ajax),  # 显示 ajax 登录页面
    path('login_ajax_check', views.login_ajax_check),  # 显示 ajax 登录页面
]
