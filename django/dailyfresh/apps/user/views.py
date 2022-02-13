import re
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin  # 用于类视图中验证用户是否登录，功能与login_required 装饰器一样

from dailyfresh import settings
from apps.user.models import User, Address
from apps.goods.models import GoodsSKU
from celery_tasks.tasks import send_activate_mail
from django_redis import get_redis_connection


# Create your views here.
# def register(request):
#     """显示注册页面"""
#     if request.method == "GET":
#         # 因为表单提交使用 post 方式的，即如果使用 get 获取的话，即为获取注册页面而不是提交表单，
#         # 所以可以靠 get 跟 post 来判断返回的是注册页面还是进行注册
#         return render(request, 'register.html')
#     else:
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#
#         # 2. 数据校验
#         if not all([username, password, email]):
#             # 检验数据不通过
#             return render(request, 'register.html', {'errmsg': '数据不完整'})
#
#         # 校验邮箱
#         if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
#             return render(request, 'register.html', {'errmsg': '邮箱不合法'})
#
#         # 检查协议
#         if allow != 'on':
#             return render(request, 'register.html', {'errmsg': '请同意协议'})
#
#         # 校验用户名是否重复
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist as exc:
#             user = None
#
#         if user:
#             # 用户已存在
#             return render(request, 'register.html', {'errmsg': '用户名已存在'})
#
#         # 3. 进行业务处理：进行用户注册
#         user = User.objects.create_user(str(username), str(email),
#                                         str(password))  # 因为使用的是 django 的认证系统，所以有 create_user 的函数可以直接使用
#         user.is_active = 0  # 使用户为非激活状态
#         user.save()
#
#         # 4. 返回应答
#         return redirect(reverse('goods:index'))


# def register_handle(request):
#     """进行注册处理"""
#
#     # 视图处理通用流程
#     # 1. 接收数据
#     username = request.POST.get('user_name')
#     password = request.POST.get('pwd')
#     email = request.POST.get('email')
#     allow = request.POST.get('allow')
#
#     # 2. 数据校验
#     if not all([username, password, email]):
#         # 检验数据不通过
#         return render(request, 'register.html', {'errmsg': '数据不完整'})
#
#     # 校验邮箱
#     if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
#         return render(request, 'register.html', {'errmsg': '邮箱不合法'})
#
#     # 检查协议
#     if allow != 'on':
#         return render(request, 'register.html', {'errmsg': '请同意协议'})
#
#     # 校验用户名是否重复
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist as exc:
#         user = None
#
#     if user:
#         # 用户已存在
#         return render(request, 'register.html', {'errmsg': '用户名已存在'})
#
#     # 3. 进行业务处理：进行用户注册
#     user = User.objects.create_user(str(username), str(email), str(password))  # 因为使用的是 django 的认证系统，所以有 create_user 的函数可以直接使用
#     user.is_active = 0  # 使用户为非激活状态
#     user.save()
#
#     # 4. 返回应答
#     return redirect(reverse('goods:index'))
# 常见请求方式 GET POST DELETE OUT OPTION
class RegisterView(View):
    """注册类视图，可以直接定义不同的方式来处理不同的请求方式"""

    def get(self, request):
        """处理 get 请求方式"""
        return render(request, 'register.html')

    def post(self, request):
        """处理 post 请求方式"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 2. 数据校验
        if not all([username, password, email]):
            # 检验数据不通过
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
            return render(request, 'register.html', {'errmsg': '邮箱不合法'})

        # 检查协议
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as exc:
            user = None

        if user:
            # 用户已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 3. 进行业务处理：进行用户注册
        user = User.objects.create_user(username, email, password)  # 因为使用的是 django 的认证系统，所以有 create_user 的函数可以直接使用
        user.is_active = 0  # 使用户为非激活状态
        user.save()

        # 4. 发送激活邮件，包含激活链接 /user/active/1
        # 激活链接中需要包含用户的身份信息，并把信息加密

        # 利用 itsdangerous 生成激活邮件的token
        serializer = Serializer(settings.SECRET_KEY, expires_in=3600)  # 第一个参数为 secret key,第二个参数为过期时间
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # 生成 token
        token = token.decode()

        # 利用 celery 发送邮件
        send_activate_mail.delay(email, username, token)

        # 5. 返回应答
        return redirect(reverse('goods:index'))


class ActivateView(View):
    """用户激活视图"""

    def get(self, request, token):

        # 1. 进行解密，获取用户信息
        serializer = Serializer(settings.SECRET_KEY, '3600')
        try:
            info = serializer.loads(token)
            # 获取待激活用户 id
            user_id = info['confirm']

            # 根据 id 获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 跳转到登录界面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse("激活链接已过期")


class LoginView(View):
    """显示登录页面"""

    def get(self, request):
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked})  # 这里的 username 和 checked 跟
        # login page 中的{{ username }} 跟 {{ checked }} 相对应，是变量名称而不是标签中的 name

    def post(self, request):
        # 1. 获取信息
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 2. 验证信息
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 3. 业务处理：登录验证
        # 因为使用了 django 的验证系统，因此以下代码来源于 django 的文档，可以直接套用
        user = authenticate(request, username=username, password=password)  # 验证用户信息，验证通过返回一个 user 的对象，不通过则返回 none，
        # 代码来源于 django 文档
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 记住用户登录状态，代码来源于 django 文档
                login(request, user)

                # 判断需要跳转的页面，如果没有则跳转到首页
                next_url = request.GET.get('next', reverse('goods:index'))
                # 跳转到对应页面
                response = redirect(next_url)  # 返回的是一个 HTTPResponseRedirect 对象

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')  # 'remember' 为标签中的 name

                if remember == "on":  # 如果 checked box 选中，返回的数值是 on
                    print(remember)
                    # 设置记住用户名的 cookie
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                # 返回应答
                return response

            else:
                return render(request, 'login.html', {'errmsg': '用户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


class LogoutView(View):
    """退出登录"""

    def get(self, request):
        # 当前请求的会话数据会完全清除。所有现有数据都将被删除
        logout(request)
        return redirect(reverse('goods:index'))


# /user
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""

    def get(self, request):
        # Django 使用 sessions 和中间件将身份验证系统挂接到请求对象中。
        # 它们在每次请求中都会提供 request.user 属性。如果当前没有用户登录，这个属性将会被设置为 AnonymousUser ，否则将会被设置为 User 实例。
        # 因此可以使用 request.user.is_authenticated 来判断用户是否登录
        # 而且 django 框架除了会给模板文件传递模板变量之外，还会把 request.user 属性传递给模板

        # 获取用户个人信息
        user = request.user
        address = Address.objects.get_default_address(user)

        # 获取用户历史浏览记录
        # 历史浏览记录保存在 redis 数据库中，当用户浏览商品详情页面的时候，会添加到数据库中
        # 而用户访问用户页面的时候，会读取前 5 条数据，数据类型为 history_用户id:[]
        con = get_redis_connection('default')  # django_redis 的方法，自动获取配置文件中 default 的 redis 数据库配置，返回一个 StrictRedis 的实例对象
        history_key = f'history_{user.id}'

        # 获取用户最新浏览的 5 个商品的 id
        sku_ids = con.lrange(history_key, 0, 4)

        # 从数据库中查询用户浏览的商品的具体信息，因为数据库获取数据会根据其自身排序，所以要用 for 循环将历史从新按照用户记录排序
        history_list = []
        for sku_id in sku_ids:
            history_good = GoodsSKU.objects.get(id=sku_id)
            history_list.append(history_good)

        # 返回应答
        return render(request, 'user_center_info.html',
                      {'page': 'user', 'address': address,
                       'history_list': history_list})  # page 参数用于判断当前用户点击的是哪个页面


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    """用户中心-订单页"""

    def get(self, request):
        # 获取用户订单信息

        return render(request, 'user_center_order.html', {'page': 'order'})


# /user/address
class AddressView(LoginRequiredMixin, View):
    """用户中心-地址页"""

    def get(self, request):
        # 获取用户默认收货地址
        user = request.user  # 因为用户在当前页面时，默认已经登录，所以可以直接从 request 中获取

        # 获取默认收货地址
        address = Address.objects.get_default_address(user)

        return render(request, 'user_center_site.html', {'page': 'address', 'address': address})

    def post(self, request):
        """添加地址"""
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg': '信息不完整'})

        if not re.match(r'(13[4-9]\d{8,})', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机号码不正确'})

        # 业务处理：地址添加
        # 如果用户已存在默认收货地址，添加地址不作为默认收货地址，否则作为默认收货地址
        user = request.user  # 因为用户在当前页面时，默认已经登录，所以可以直接从 request 中获取

        # 获取默认收货地址
        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(user=user, receiver=receiver, addr=addr, is_default=is_default, zip_code=zip_code,
                               phone=phone)

        # 返回应答，刷新页面
        return redirect(reverse("user:address"))  # 重定向默认使用 get
