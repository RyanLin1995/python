# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
# 以下一个最简单的Web版本的“Hello World!”：

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'Hello World!'

# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象
# start_response：一个发送HTTP响应的函数

# application()函数必须由WSGI服务器来调用，因此参数也由WSGI服务器提供
