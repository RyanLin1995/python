from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
# 1. 创建蓝图对象
bp = Blueprint('bp', __name__)
# 2. api 绑定 bp
api = Api(bp)


class HelloWorldResource(Resource):
    """
        资源
    """

    def get(self):
        return {'get': 'hello world'}

    def post(self):
        return {'post': 'post hello world'}


# 3. 利用蓝图里面的 api 对象来收集路径信息
api.add_resource(HelloWorldResource, '/', endpoint='HelloWorld')

# 4. 注册蓝图到 app 中
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
