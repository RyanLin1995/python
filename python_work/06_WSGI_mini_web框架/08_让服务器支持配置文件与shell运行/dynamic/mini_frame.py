def index():

    with open("./templates/index.html", encoding='UTF-8') as f:  # 这里用了 ./ 而不是使用 ../ 的原因是：该模块是被web_server调用的，因此程序运行时应该是以web_server这个模块的位置作为根目录
        return f.read()


def center():

    with open("./templates/center.html", encoding='UTF-8') as f:
        return f.read()


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World!'

