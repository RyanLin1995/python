from flask import Flask

# Flask将配置信息保存到了 app.config 属性中，该属性可以按照字典类型进行操作
# 读取
# app.config.get(name)
# app.config[name]

# 设置
# 主要使用以下三种方式：
# 1. 从配置对象中加载
# app.config.from_object(配置对象)
# class DefaultConfig(object):
#     """默认配置"""
#     SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'

# 2. 从配置文件中加载
# app.config.from_pyfile(配置文件)
# 新建一个配置文件setting.py
# SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'

# 3. 从环境变量中加载
# Flask使用环境变量加载配置的本质是通过环境变量值找到配置文件，再读取配置文件的信息，其使用方式为
# app.config.from_envvar('环境变量名')

app = Flask(__name__, static_url_path='/s')


# app.config.from_object(DefaultConfig)  # 1. 从配置对象中加载
# app.config.from_pyfile('setting.py')  # 2. 从配置文件中加载
# app.config.from_envvar('test', silent=True)  # 3. 从环境变量中加载，一般填写配置文件路径。从环境变量指向的配置文件中读取的配置信息会覆盖掉从配置对象中加载的同名参数
# 关于silent的说明：表示系统环境变量中没有设置相应值时是否抛出异常，
# False 表示不安静的处理，没有值时报错通知，默认为False
# True 表示安静的处理，即时没有值也让Flask正常的运行下去

# 定义视图
@app.route('/')
def index():
    print(app.config['test'])
    return 'test'


if __name__ == '__main__':
    app.run()
