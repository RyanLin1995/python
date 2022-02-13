from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cart'  # 因为是子文件夹，所以 app 的 name 要完整路径
