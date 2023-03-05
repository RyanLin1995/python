from flask import Flask, abort, request

app = Flask(__name__)


# HTTP 异常主动抛出
# abort 方法
# 抛出一个给定状态代码的 HTTPException 或者指定响应，例如想要用一个页面未找到异常来终止请求，你可以调用 abort(404)。

@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')

    if channel_id is None:
        abort(400)  # 错误时显示 400 状态码

    return f"Your channel id is {channel_id}."


# 捕获错误
# errorhandler 装饰器
# 注册一个错误处理程序，当程序抛出指定错误状态码的时候，就会调用该装饰器所装饰的方法
# 参数：
# code_or_exception – HTTP的错误状态码或指定异常
@app.errorhandler(500)
def internal_server_error(e):  # 必须传递参数 e，e 是错误类型
    return '服务器不见了'


@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'


@app.route('/error')
def raise_error():
    1 / 0

    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
