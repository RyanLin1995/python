from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)

api = Api(app)


class DemoResource(Resource):
    def get(self):
        # RequestParser类，用来帮助我们检验和转换请求数据，步骤如下：
        # 1. 创建 RequestParser 对象
        rq = RequestParser()
        # 2. 声明参数
        # 参数说明
        # (1)required
        # 描述请求是否一定要携带对应参数，默认值为False
        # True:强制要求携带
        # 若未携带，则校验失败，向客户端返回错误信息，状态码400
        # False:不强制要求携带
        # 若不强制携带，在客户端请求未携带参数时，取出值为None
        #
        # (2)help
        # 参数检验错误时返回的错误描述信息
        #
        # (3)action
        # 描述对于请求参数中出现多个同名参数时的处理方式
        # action = 'store' # 保留出现的第一个， 默认
        # action = 'append' # 以列表追加保存所有同名参数的值
        #
        # (4)type
        # 描述参数应该匹配的类型，可以使用python的标准数据类型string、int，也可使用 Flask - RESTful 提供的检验方法，还可以自己定义
        # 标准类型
        # rp.add_argument('a', type=int, required=True, help='missing a param', action='append')
        # Flask - RESTful提供
        # 检验类型方法在flask_restful.inputs模块中
        # * url
        #
        # * regex(指定正则表达式)
        # from flask_restful import inputs
        # rp.add_argument('a', type=inputs.regex(r'^\d{2}&'))
        #
        # * natural  # 自然数0、1、2、3...
        #
        # * positive  # 正整数 1、2、3...
        #
        # * int_range(low, high)  # 整数范围
        # rp.add_argument('a', type=inputs.int_range(1, 10))
        #
        # * boolean
        #
        # * 自定义
        # def mobile(mobile_str):
        #     """
        #     检验手机号格式
        #     :param mobile_str: str 被检验字符串
        #     :return: mobile_str
        #     """
        #     if re.match(r'^1[3-9]\d{9}$', mobile_str):
        #         return mobile_str
        #     else:
        #         raise ValueError('{} is not a valid mobile'.format(mobile_str))
        #
        # rq.add_argument('a', type=mobile)
        #
        # (5)location
        # 描述参数应该在请求数据中出现的位置
        # Look only in the POST body
        # rq.add_argument('name', type=int, location='form')
        #
        # # Look only in the querystring
        # rq.add_argument('PageSize', type=int, location='args')
        #
        # # From the request headers
        # rq.add_argument('User-Agent', location='headers')
        #
        # # From http cookies
        # rq.add_argument('session_id', location='cookies')
        #
        # # From json
        # rq.add_argument('user_id', location='json')
        #
        # # From file uploads
        # rq.add_argument('picture', location='files')
        # # 也可指明多个位置
        # rq.add_argument('text', location=['headers', 'json'])

        rq.add_argument('a', location='args')
        rq.add_argument('b', location='args')
        # 3. 执行检验
        req = rq.parse_args()
        # req 既可以当作字典，也可以当作对象
        rq_a = req['a']
        rq_a = req.a
        return {'msg': rq_a}


api.add_resource(DemoResource, '/demo')

if __name__ == '__main__':
    app.run(debug=True)
