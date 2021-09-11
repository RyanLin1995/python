from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from booktest.models import BookInfo


# Create your views here.
def my_render(request, template_path, context_dict=None):
    """使用模板文件"""
    # 1. 加载模板文件，返回的是模板对象
    tp = loader.get_template(template_path)  # 传入模板的路径，是一个相对路径，相对于在setting里面设置的模板目录

    # 2. 定义模板上下文：给模板文件传递数据(2.0以下 django 有用)
    context = RequestContext(request, context_dict)  # 第一个参数是 request，第二个参数是一个字典，填写的是要传递的数据，没有数据可以填空

    # 3. 模板渲染：产生标准的 html 内容，2.0以下 django 传递的是模板上下文的实例对象，2.0以上直接传递需要修改的数据。返回一个替换数据后的 html 文件
    res_html = tp.render(context_dict)

    # 4. 返回给浏览器
    return HttpResponse(res_html)


def index(request):
    # return my_render(request, 'booktest/index.html')  # 这是我们自己写的函数
    return render(request, 'booktest/index.html')  # 实际上 django 已经帮我们写好函数，就是 render， 其返回值是 HttpResponse 的子类


def temp_args(request):
    """模板变量"""
    my_dict = {"title": "字典键值"}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)
    context = {'my_dict': my_dict, 'my_list': my_list, 'book': book}
    return render(request, "booktest/temp_args.html", context)


def temp_tags(request):
    """模板标签"""
    books = BookInfo.objects.all()
    return render(request, "booktest/temp_tags.html", {"books": books})


def temp_filter(request):
    """模板标签"""
    books = BookInfo.objects.all()
    return render(request, "booktest/temp_filter.html", {"books": books})