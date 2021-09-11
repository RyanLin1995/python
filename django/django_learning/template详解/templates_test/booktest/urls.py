from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('index/', views.index),
    path('temp_args/', views.temp_args),
    path('temp_tags/', views.temp_tags),
    path('temp_filter/', views.temp_filter),
]
