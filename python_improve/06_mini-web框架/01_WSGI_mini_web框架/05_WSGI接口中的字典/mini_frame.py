def index():

    return "这是主页"


def login():

    return "这是登录界面"


# application 中的第一个形参(这里是environ)接收来自浏览器的 request 信息，如 'GET /classic.css HTTP/1.1'
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World!'

