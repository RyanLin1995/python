import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from django.views import View

from booktest.models import BookInfo


def my_render(request, template_path, context_dict=None):
    """使用模板文件"""
    # 1. 加载模板文件，返回的是模板对象
    tp = loader.get_template(template_path)  # 传入模板的路径，是一个相对路径，相对于在setting里面设置的模板目录

    # 2. 定义模板上下文：给模板文件传递数据(2.0以下 django 有用)
    context = RequestContext(request, context_dict)  # 第一个参数是 request，第二个参数是一个字典，填写的是要传递的数据，没有数据可以填空

    # 3. 模板渲染：产生标准的 html 内容，2.0以下 django 传递的是模板上下文的实例对象，2.0以上直接传递需要修改的数据。返回一个替换数据后的 html 文件
    res_html = tp.render({})

    # 4. 返回给浏览器
    return HttpResponse(res_html)


# Create your views here.
# 1. 定义视图函数，需要加一个 request 参数
# 2. 进行 URL 配置，建立 URL 地址和视图的对应关系
def index(request):
    # return HttpResponse("Hello World")
    # return my_render(request, 'booktest/index.html')  # 自己写的 render 函数
    return render(request, 'booktest/index.html',
                  {'content': 'hello world', 'list': list(range(1, 10))})  # 实际开发用的 render 函数


def index2(request):
    return HttpResponse("Hello Python")


# 综合案例
def show_books(request):
    """显示图书的信息"""
    # 1. 通过 M 查找图书表中的信息
    books = BookInfo.objects.all()

    # 2. 使用模板
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    """查询图书关联的英雄信息"""
    # 1. 根据 bid 查询图书信息
    book = BookInfo.objects.get(id=bid)

    # 2. 查询图书 book 相关的英雄信息
    heros = book.heroinfo_set.all()

    # 3. 使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})


class AxiosShow(View):
    def get(self, request):
        return render(request, 'booktest/09_axios.html')


class AxiosText(View):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username == '123' and password == '123':
            return JsonResponse({'code': 200, 'msg': 'OK', 'username': username})
        else:
            return JsonResponse({'code': 400, 'msg': 'Fail'})

    def post(self, request):
        print(request.body)
        # 因为 post 传过来的是 json，所以需要 decode 并用 json 读取
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)

        if username == '123' and password == '123':
            return JsonResponse({'code': 200, 'msg': 'OK', 'username': username})
        else:
            return JsonResponse({'code': 400, 'msg': 'Fail'})
