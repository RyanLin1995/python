from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


# Create your views here.
# request是HttpRequest类型的对象，包含浏览器请求的信息
def index(request):
    """首页"""
    # num = 'a' + 1  # 错误视图示范
    return render(request, 'booktest/index.html')


def show_args(request, num):
    return HttpResponse(num)


def login(request):
    """显示登录页面"""
    # 判断用户是否登录
    if request.session.has_key('is_login'):
        return redirect("/index")
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
    # 2. 进行登录的校验
    # 实际开发下，根据用户名跟密码查找数据库
    # 以下是模拟
    if username == 'admin' and password == '123':
        # 用户名密码正确，跳转到首页
        response = redirect('/index')
        # 判断是否记住用户名
        if remember == "on":
            response.set_cookie("username", username, max_age=7*24*3600)

        # 记住用户登录状态
        # 只要 session 存在 is_login 就认为用户已登录
        request.session['is_login'] = True
        return response
    else:
        # 密码错误，回到登录页面
        return redirect('/login')


def ajax_test(request):
    """显示 ajax 页面"""
    return render(request, 'booktest/ajax_test.html')


def ajax_handle(request):
    """ajax 请求处理"""
    # 返回的 json 数据 {'ret':1}，会自动转为 json 数据
    # num = 'a' + 1  # 模拟 ajax 错误，ajax 错误要在开发者模式---> network ---> 对应 url ---> preview 中查看
    return JsonResponse({'ret': 1})


def login_ajax(request):
    """显示 ajax 登录页面"""
    return render(request, 'booktest/login_with_ajax.html')


def login_ajax_check(request):
    """ajax 登录校验"""
    # 1. 获取用户名跟密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2. 进行校验，返回 json 数据
    if username == 'admin' and password == '123':
        # 用户名密码正确
        return JsonResponse({'ret': 1})  # 这里不能用 redirect，因为 ajax 所有操作都是在后台，redirect 的数据是在后台进行了，没显示在浏览器
    else:
        # 用户名或密码错误
        return JsonResponse({'ret': 0})


# /set_cookie
def set_cookie(request):
    """设置 cookie"""
    response = HttpResponse("设置 cookie")
    # 设置一个 cookie 值，名称为 num, 值为 1
    # max_age 跟 expires 都可以设置过期时间
    # max_age 后面接秒数(max_age=14*24*3600)  # 两周后过期
    # expires 后面接现在日期+多少天后过期(datetime.now()+timedelta(days=14))  # 两周后过期
    response.set_cookie('num', 1, max_age=14*24*3600)  # 无论设置什么值，都是字符串
    # 返回 response
    return response


# /get_cookie
def get_cookie(request):
    """获取 cookie 值"""
    # 取出 cookie 值
    num = request.COOKIES['num']
    return HttpResponse(num)


# /set_session
def set_session(request):
    """设置 session """
    request.session['username'] = 'admin'
    request.session['age'] = 18
    request.session.set_expiiry(5)  # 设置过期时间，参数是秒数，如果设置0为关闭浏览器即删除；None为永不过期
    return HttpResponse("设置session")


# /get_session
def get_session(request):
    """获取 session """
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ":" + str(age))


# /clear_session
def clear_session(request):
    """清除 session """
    # request.session.clear()  # 清除 session 保存的 value
    request.session.flush()  # 在数据库清除 session
    return HttpResponse("清除成功")