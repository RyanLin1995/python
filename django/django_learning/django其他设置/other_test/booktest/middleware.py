from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin  # 兼容 Django 旧版类


class BlockIPSMiddleware(object):
    exclude_ips = ['192.168.1.99']

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        """新版中间件返回值的写法"""

        # 以下是视图函数调用前会运行的代码
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in self.exclude_ips:
            return HttpResponse("<h1>Forbidden</h1>")

        response = self.get_response(request)

        # 以下是视图函数调用后，request/response函数调用前会运行的代码

        return response


class TestMiddleware(MiddlewareMixin):
    """旧版中间件类的写法，继承于 MiddlewareMixin 用以兼容之前的代码"""
    def __init__(self, get_response):  # 中间件函数必须接受 get_response 参数
        """服务器重启后接收第一个请求时调用"""
        self.get_response = get_response
        print("--init--")

    def process_request(self, request):
        """产生request对象后，url匹配前调用"""
        print("--process_request--")
        # return HttpResponse("process_request")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配后，视图函数调用前调用"""
        print("--process_view--")
        return HttpResponse("process_view")

    def process_response(self, request, response):
        """视图函数调用之后，内容返回浏览器之前调用"""
        print("--process_response--")
        return response


class ExceptionTest1Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print("--process_exception1--")
        print(exception)

    def __call__(self, request):
        response = self.get_response(request)
        return response


class ExceptionTest2Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print("--process_exception2--")

    def __call__(self, request):
        response = self.get_response(request)
        return response
