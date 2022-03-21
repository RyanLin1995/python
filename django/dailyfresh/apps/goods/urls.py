from django.urls import path, re_path
from apps.goods.views import IndexView, DetailVIew, ListView

urlpatterns = [
    path("index", IndexView.as_view(), name='index'),
    re_path(r"goods/(?P<goods_id>\d+)$", DetailVIew.as_view(), name='detail'),
    re_path(r"list/(?P<type_id>\d+)/(?P<page>\d+)$", ListView.as_view(), name='list')
]
