from django.urls import path, re_path
from django.contrib.auth.decorators import login_required  # 用于判断用户是否登录的方法

from apps.user.views import RegisterView, ActivateView, LoginView, UserInfoView, UserOrderView, AddressView, LogoutView

urlpatterns = [

    path('register', RegisterView.as_view(), name="register"),  # 注册页面
    re_path(r'^activate/(?P<token>.*)$', ActivateView.as_view(), name="activate"),  # 注册页面
    path('login/', LoginView.as_view(), name="login"),  # 登录页面
    path('logout/', LogoutView.as_view(), name="logout"),  # 退出登录

    # 因为是登录后才能访问的，且 view 的处理是类，所以需要在 as_view 加上
    # path('', login_required(UserInfoView.as_view()), name="user"),  # 用户中心-信息页面
    # path('order', login_required(UserOrderView.as_view()), name="order"),  # 用户中心-订单页面
    # path('address', login_required(AddressView.as_view()), name="address"),  # 用户中心-地址页面
    # 但是在类视图中继承了 LoginRequiredMixin 类，所以不需要再加上装饰器了 login_required 装饰器.
    path('', UserInfoView.as_view(), name="user"),  # 用户中心-信息页面
    re_path(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name="order"),  # 用户中心-订单页面
    path('address', AddressView.as_view(), name="address"),  # 用户中心-地址页面


    # 因为会使用类视图来处理注册，所以以下代码注释掉
    # path('register', views.register, name="register"),  # 注册页面

    # 因为注册和处理用同一地址，所以以下代码注释掉
    # path('register_handler', views.register_handle, name="register_handle")  # 注册处理
]
