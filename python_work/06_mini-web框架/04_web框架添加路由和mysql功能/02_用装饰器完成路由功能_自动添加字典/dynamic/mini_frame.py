import re
import time

URL_FUNC_DICT = {}  # 该字典其实是一个映射


# 利用带参数的装饰器，把第一个参数作为 key，要被装饰的参数指向作为 value 传到字典中
def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route('/index.py')
def index():

    with open("./templates/index.html", encoding='UTF-8') as f:  # 这里用了 ./ 而不是使用 ../ 的原因是：该模块是被web_server调用的，因此程序运行时应该是以web_server这个模块的位置作为根目录
        content = f.read()
    my_stock_info = "这是MYSQL查询出来的数据"

    content = re.sub(r'{%content%}', my_stock_info, content)

    return content


@route('/center.py')
def center():

    with open("./templates/center.html", encoding='UTF-8') as f:
        content = f.read()
    now = time.ctime()
    my_stock_info = str(now)

    content = re.sub(r'{%content%}', my_stock_info, content)

    return content


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]

    try:
        return URL_FUNC_DICT[file_name]()  # 根据不同的内容调用不同的函数去处理，该功能称为路由
    except Exception as ret:
        return "产生了异常:{}".format(ret)


