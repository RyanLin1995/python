from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.urls import reverse
from booktest.models import BookInfo


# Create your views here.
def login_required(view_func):
    """判断登录的装饰器"""

    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('is_login'):
            # 用户已登录，调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户为登录，跳转到登录页
            return redirect('/login')

    return wrapper


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


def temp_inherit(request):
    """模板继承"""
    return render(request, 'booktest/child.html')


def html_escape(request):
    """html转义"""
    return render(request, 'booktest/html_escape.html', {'content': '<h1>hello</h1>'})


def login(request):
    """显示登录页面"""
    # 判断用户是否登录
    if request.session.has_key('is_login'):
        return redirect("/change_pwd")
    else:
        # 获取 cookie 的用户名
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {"username": username})


def login_check(request):
    """登录校验视图"""
    # request.POST 保存的是 post 方式提交的参数，返回的是 QueryDict 对象。
    # request.GET 保存的是 get 方式提交的参数，返回的是 QueryDict 对象。
    # QueryDict 类似于字典，但是可以多个同样的 key 对不同的 value, 可以通过 getlist('keyname') 获取

    # 1. 获取提交的用户名和密码
    username = request.POST['username']  # POST['username'] 中的 username 跟为 input 中的 name='username'，两者参数必须一样
    password = request.POST['password']
    remember = request.POST.get('remember')

    # 获取用户输入的验证码
    vcode1 = request.POST.get('vcode')
    # 获取 session 中保存的验证码
    vcode2 = request.session.get('verifycode')
    # 进行验证码校验
    if vcode1 != vcode2:
        # 验证码错误
        return redirect('/login')

    # 2. 进行登录的校验
    # 实际开发下，根据用户名跟密码查找数据库
    # 以下是模拟
    if username == 'admin' and password == '123':
        # 用户名密码正确，跳转到首页
        response = redirect('/change_pwd')
        # 判断是否记住用户名
        if remember == "on":
            response.set_cookie("username", username, max_age=7 * 24 * 3600)

        # 记住用户登录状态
        # 只要 session 存在 is_login 就认为用户已登录
        request.session['is_login'] = True
        # 记住登录的用户名
        request.session['username'] = username
        return response
    else:
        # 密码错误，回到登录页面
        return redirect('/login')


@login_required
def change_pwd(request):
    """显示修改密码页面"""
    # 进行用户是否登录的判断
    # if not request.session.has_key('login'):
    #     # 用户未登录，跳转到登录页面
    #     return redirect('/login')
    return render(request, "booktest/change_pwd.html")


@login_required
def change_pwd_action(request):
    """模拟修改密码"""
    # 1. 获取新密码
    pwd = request.POST.get('pwd')
    # 获取用户名
    username = request.session['username']
    # 2. 实际开发的时候：修改对应数据库的内容
    # 3. 返回应答
    return HttpResponse(f'{username}修改密码为:{pwd}')


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bg_color = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bg_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype(r'/usr/share/fonts/truetype/unifont/unifont.ttf', 23)
    # 构造字体颜色
    font_color = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=font_color)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color)
    draw.text((50, 2), rand_str[2], font=font, fill=font_color)
    draw.text((75, 2), rand_str[3], font=font, fill=font_color)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def url_reverse(request):
    """ URL反向解析 """
    return render(request, "booktest/url_reverse.html")


def show_args(request, a, b):
    return HttpResponse(a+":"+b)


def show_kwargs(request, c, d):
    return HttpResponse(c+":"+d)


def test_redirect(request):
    """重定向到首页"""
    # return redirect('/index')
    # url = reverse('booktest:index')
    # return redirect(url)

    # 重定向到/show_args/1/2
    # url = reverse('booktest:show_args', args=(1, 2))
    # return redirect(url)

    # 重定向到/show_kwargs/3/4
    url = reverse('booktest:show_kwargs', kwargs={'c': 3, 'd': 4})
    return redirect(url)