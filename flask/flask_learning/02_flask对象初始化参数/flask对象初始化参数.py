from flask import Flask

# Flask 应用程序在创建的时候一些需要我们关注的参数：
# import_name
# * Flask程序所在的包(模块)，传 __name__ 就可以
# * 其可以决定 Flask 在访问静态文件时查找的路径
# static_url_path
# * 静态文件访问路径，可以不传，默认为：/ + static_folder
# static_folder
# * 静态文件存储的文件夹，可以不传，默认为 static
# template_folder
# * 模板文件存储的文件夹，可以不传，默认为 templates
app = Flask(__name__, static_url_path='/s')


# 定义视图
@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
