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
]
