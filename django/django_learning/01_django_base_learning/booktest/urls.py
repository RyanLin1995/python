from django.urls import path, re_path
from booktest import views

# 在应用里面新建该文件，文件名固定为 urls ，文件内容格式固定如下
urlpatterns = [

    # 通过 path 函数设置 url 路由配置项
    path('index/', views.index),  # 建立 /index 链接与视图 index 之间的联系，建议在第一个参数后加上 /
    path('index2/', views.index2),
    path('books/', views.show_books),  # 显示图书信息
    re_path('books/(\d+)', views.detail),
    path('show/', views.AxiosShow.as_view()),
    path('axiostest/', views.AxiosText.as_view())
]
