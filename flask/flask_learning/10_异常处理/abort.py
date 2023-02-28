from flask import Flask, abort, request

app = Flask(__name__)


# abort 方法
# 抛出一个给定状态代码的 HTTPException 或者指定响应，例如想要用一个页面未找到异常来终止请求，你可以调用 abort(404)。

@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')

    if channel_id is None:
        abort(400)  # 错误时显示 400 状态码

    return f"Your channel id is {channel_id}."


if __name__ == '__main__':
    app.run(debug=True)
