from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),  # 新增一本图书
    re_path(r'delete(\d+)/', views.delete),  # 删除点击的图书
    path('areas/', views.areas)
]
