import datetime
from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo, AreaInfo
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def index(request):
    """显示图书信息"""
    # 1. 查询所有图书信息
    books = BookInfo.objects.all()
    # 2. 使用模板
    return render(request, 'booktest/index.html', {"books": books})


def create(request):
    """新增图书"""
    # 1. 创建BookInfo对象
    b = BookInfo()
    b.btitle = "流星蝴蝶剑"
    b.bpub_date = datetime.datetime(1990, 1, 1)
    # 2. 保存到数据库
    b.save()
    # 3. 返回应答，让浏览器再访问 /index，即重定向
    # return HttpResponse('OK')
    # return HttpResponseRedirect('/index')
    return redirect('/index')  # return HttpResponseRedirect('/index') 的简写


def delete(request, bid):
    """删除点击的图书"""
    # 1. 通过 bid 获取图书对象
    b = BookInfo.objects.get(id=bid)
    # 2. 删除
    b.delete()
    # 3. 重定向，让浏览器访问 /index
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def areas(request):
    """获取广州市上级地区和下级地区"""
    # 1. 获取广州市的信息
    area = AreaInfo.objects.get(atitle="广州市")
    # 2. 查询广州市的上级地区(由多查1)
    parent = area.aParent
    # 3. 查询广州市的下级地区(由1查多)
    children = area.areainfo_set.all()
    # 4. 使用模板
    return render(request, 'booktest/areas.html', {"area": area, "parent": parent, "children": children})
