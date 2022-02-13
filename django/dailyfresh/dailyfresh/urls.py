"""dailyfresh URL Configuration

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
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),  # 增加富文本编辑器 url
    path(r'cart/', include(('apps.cart.urls', 'cart'))),
    path(r'order/', include(('apps.order.urls', 'order'))),
    path(r'user/', include(('apps.user.urls', 'user'))),
    re_path(r'^', include(('apps.goods.urls', 'goods'))),  # 因为是第一个匹配的所以要放在最后边
]
