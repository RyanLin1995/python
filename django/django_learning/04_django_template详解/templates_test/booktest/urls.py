from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('index123/', views.index, name='index'),
    path('temp_args/', views.temp_args),
    path('temp_tags/', views.temp_tags),
    path('temp_filter/', views.temp_filter),
    path('temp_inherit/', views.temp_inherit),
    path('html_escape/', views.html_escape),
    path('login/', views.login),
    path('login_check', views.login_check),
    path('change_pwd/', views.change_pwd),
    path('change_pwd_action', views.change_pwd_action),
    path('verify_code/', views.verify_code),
    path('url_reverse/', views.url_reverse),
    re_path(r'show_args/(\d+)/(\d+)', views.show_args, name='show_args'),
    re_path(r'show_kwargs/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs, name='show_kwargs'),
    path('test_redirect', views.test_redirect),
]
