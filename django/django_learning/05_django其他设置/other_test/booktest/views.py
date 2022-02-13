import json
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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


# 前端访问的时候需要传递页码
def show_area(request, pindex):
    """分页"""
    # 1. 查询出所有省级地区的信息
    area_list = models.AreaInfo.objects.filter(aParent__isnull=True).order_by('id')  # 因为 Paginator 要求 query_set 是有序的，所以需要对 object_list 进行排序
    # 2. 分页
    paginator_object = Paginator(area_list, 10)
    # 3. 获取第 pindex 页的内容
    if pindex == '':
        # 默认取第一页的内容
        pindex = 1
    else:
        pindex = int(pindex)

    # page 是 Page 类的实例对象
    page_object = paginator_object.page(int(pindex))

    # 4. 使用模板
    return render(request, 'booktest/show_area.html', {'page_object': page_object})


def areas(request):
    """省市县案例"""
    return render(request, 'booktest/areas.html')


def prov(request):
    """获取所有省级地区的信息"""
    # 1. 查询出所有省级地区的信息，并将 queryset 转化为 json
    area_list = list(models.AreaInfo.objects.filter(aParent__isnull=True).order_by('id').values())  # values() 方法返回一组表示模型实例的字典
    # 2. 返回数据
    return JsonResponse({'data': area_list}, safe=False)


def city(request, pid):
    """获取 pid 地区下级地区的信息"""
    # 1. 获取 pid 对应地区的下级地区
    # area = models.AreaInfo.objects.get(id=pid)
    # area_list = area.areainfo_set.all()
    area_list = list(models.AreaInfo.objects.filter(aParent=pid).order_by('id').values())

    # 2. 返回数据
    return JsonResponse({'data': area_list}, safe=False)