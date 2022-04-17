from django.urls import path, re_path
from apps.cart.views import CartAddView, CartInfoView, CartUpdateView, CartDeleteView

urlpatterns = [
    path('add', CartAddView.as_view(), name='add'),  # 购物车记录添加
    path('update', CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    path('delete', CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
    re_path(r"^$", CartInfoView.as_view(), name='show'),  # 购物车记录展示
]
