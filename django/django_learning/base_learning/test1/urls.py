"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 项目的 urls 文件
urlpatterns = [
    path('admin/', admin.site.urls),  # 配置项
    path(r'', include('booktest.urls'))  # 包含 booktest 应用的 urls 文件。使用 path 后，第一个 router 参数应该是URL 模式，是一个字符串，旧版 jdango
    # 中的 url 函数第一个参数传入的是正则表达式。 如果想要在新版中使用正则表达式，可以用 re_path 函数
]
