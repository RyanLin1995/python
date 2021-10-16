from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('static_test', views.static_test),
    path('index/', views.index),
    path('upload_pic/', views.upload_pic),
    re_path('^upload_pic_handle$', views.upload_pic_handle),
    re_path(r'^show_area(?P<pindex>\d*)', views.show_area),
    path(r'areas/', views.areas),
    path(r'prov/', views.prov),
    re_path(r'^city(\d+)', views.city),
    re_path(r'^dis(\d+)', views.city),  # 因为 city 跟 dis 获取内容的过程一致，所以可以直接使用 city 的 views
]
