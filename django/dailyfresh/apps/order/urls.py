from django.urls import path, include
from apps.order.views import OrderPlaceView, OrderCommitView

urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),
    path('commit', OrderCommitView.as_view(), name='commit'),
]
