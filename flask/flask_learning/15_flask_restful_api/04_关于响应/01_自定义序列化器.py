from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields, marshal

app = Flask(__name__)

api = Api(app)


# 用来模拟要返回的数据对象的类
class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


# 声明需要序列化处理的字段
resource_fields = {
    'uid': fields.Integer,
    'name': fields.String
}


class Demo1Resource(Resource):
    # 装饰器的方式将数据序列化为特定格式 marshal_with 为 marshal 的封装
    @marshal_with(resource_fields, envelope='data1')  # envelope 参数为将返回的数据内嵌到 envelope 字典中
    def get(self):
        user = User(1, 'test1', 18)
        return user


class Demo2Resource(Resource):
    def get(self):
        user = User(2, 'test2', 20)
        return marshal(user, resource_fields)


api.add_resource(Demo1Resource, '/demo1')
api.add_resource(Demo2Resource, '/demo2')

if __name__ == '__main__':
    app.run(debug=True)
