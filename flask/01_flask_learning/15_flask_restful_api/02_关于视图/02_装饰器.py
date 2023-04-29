from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return wrapper


class HelloWorldResource(Resource):
    # 使用 method_decorators 为所有视图中的方法添加装饰器
    method_decorators = [decorator1, decorator2]

    # method_decorators 效果类似于以下
    # @decorator2
    # @decorator1
    # def get(self):
    #     ...

    def get(self):
        return {'get': 'hello world'}

    def post(self):
        return {'post': 'hello world'}


api.add_resource(HelloWorldResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
