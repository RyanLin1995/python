from flask import Flask, g, abort

app = Flask(__name__)


@app.before_request
def authentication():
    """
    利用 before_request 请求钩子，在进入所有视图前先尝试判断用户身份
    :return:
    """
    # TODO 此处利用鉴权机制（如cookie、session、jwt等）鉴别用户身份信息
    # if 已登录用户，用户有身份信息
    g.user_id = 123
    # else 未登录用户，用户无身份信息
    # g.user_id = None


def login_check(func):
    def wrapper(*args, **kwargs):
        if g.user_id is not None:
            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper


@app.route('/')
def index():  # 普通视图，不要求用户登录
    return 'home page user_id={}'.format(g.user_id)


@app.route('/get_user')
@login_check
def get_user_id():  # 用户视图，需要登录才可以访问
    return 'user profile page user_id={}'.format(g.user_id)


if __name__ == '__main__':
    app.run(debug=True)
