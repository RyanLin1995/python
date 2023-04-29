from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorldResource(Resource):
    """
        资源
    """

    def get(self):
        return {'get': 'hello world'}

    def post(self):
        return {'post': 'post hello world'}


api.add_resource(HelloWorldResource, '/', endpoint='HelloWorld')  # 注册资源到 api，endpoint 为 url 别名
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
