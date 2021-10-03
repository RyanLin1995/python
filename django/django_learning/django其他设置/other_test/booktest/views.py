from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from booktest import models

# Create your views here.
exclude_ips = ['192.168.1.99']


def block_ips(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in exclude_ips:
            return HttpResponse("<h1>Forbidden</h1>")
        else:
            return view_func(request, *view_args, **view_kwargs)

    return wrapper


# @block_ips
def static_test(request):
    """静态文件"""
    return render(request, 'booktest/static_test.html')


# @block_ips
def index(request):
    """首页"""
    # 获取浏览器端的ip地址
    print("index")
    num = 'a' + 1
    return render(request, 'booktest/index.html')


def upload_pic(request):
    """显示上传图片页面"""
    return render(request, 'booktest/upload_pic.html')


def upload_pic_handle(request):
    """上传图片处理"""
    # 1.获取上传的文件的处理对象
    pic_object = request.FILES.get('pic')

    # 2.创建文件
    file_path = fr"{settings.MEDIA_ROOT}/booktest/{pic_object.name}"
    with open(file_path, 'wb') as f:
        # 3.获取上传文件的内容并写入创建的文件中
        for content in pic_object.chunks():  # pic_object.chunks() 是一个生成器，会不断返回图片的数据
            f.write(content)

    # 4.保存记录到数据库
    models.PicTest.objects.create(goods_pic=fr'booktest/{pic_object.name}')  # 用 create 方法创建表数据，等价与 save()
    # 5.返回
    return HttpResponse('ok')