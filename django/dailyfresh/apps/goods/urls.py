from django.urls import path, re_path
from apps.goods.views import IndexView, DetailVIew

urlpatterns = [
    path("index", IndexView.as_view(), name='index'),
    re_path(r"goods/(?P<goods_id>\d+)$", DetailVIew.as_view(), name='detail'),
]
