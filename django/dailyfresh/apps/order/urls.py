from django.urls import path, re_path
from apps.order.views import OrderPlaceView, OrderCommitView, OrderPayView, CheckPayView, CommentView

urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),
    path('commit', OrderCommitView.as_view(), name='commit'),
    path('pay', OrderPayView.as_view(), name='pay'),
    path(r'check', CheckPayView.as_view(), name='check'),  # 查询支付交易结果
    re_path(r'comment/(?P<order_id>.+)$', CommentView.as_view(), name='comment'),  # 订单评论
]
