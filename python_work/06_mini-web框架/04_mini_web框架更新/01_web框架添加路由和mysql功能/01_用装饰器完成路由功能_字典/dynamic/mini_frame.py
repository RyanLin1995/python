import re
import time


def index():

    with open("./templates/index.html", encoding='UTF-8') as f:  # 这里用了 ./ 而不是使用 ../ 的原因是：该模块是被web_server调用的，因此程序运行时应该是以web_server这个模块的位置作为根目录
        content = f.read()
    my_stock_info = "这是MYSQL查询出来的数据"

    content = re.sub(r'{%content%}', my_stock_info, content)

    return content


def center():

    with open("./templates/center.html", encoding='UTF-8') as f:
        content = f.read()
    now = time.ctime()
    my_stock_info = str(now)

    content = re.sub(r'{%content%}', my_stock_info, content)

    return content


URL_FUNC_DICT = {
    "index.py": index,
    "center.py": center
}  # 使用字典的方式替代 application 函数中的if


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]

    func = URL_FUNC_DICT[file_name]
    return func()

