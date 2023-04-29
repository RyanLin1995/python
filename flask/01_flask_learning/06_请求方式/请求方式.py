from flask import Flask

app = Flask(__name__)


# 请求方式
# GET
# OPTIONS(自带）->简化版的GET请求用于询问服务器接口信息的，比如接口允许的请求方式充许的请求源头域名
#   CORS 跨域处理 django-corst(django中间件,用于拦截并处理 option 请求)
#   从 www.meiduo.site 访问 api.meiduo.site/users/1
#   1. 先发送 options 到 api.meiduo.site/uses/1
#   2. 检查白名单，存在即返回 response -> allow-origin'www.meiduo.site
#   3. GET api.meiduo.site/users/1
# HEAD（自带）简化版的GET请求，只返回GET请求处理时的响应头头，不返回响应体

# methods 指定请求方式
@app.route('/', methods=['POST'])
def index():
    return 1


if __name__ == '__main__':
    app.run(debug=True)
