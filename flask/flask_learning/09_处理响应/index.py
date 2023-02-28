from flask import Flask, render_template, redirect, jsonify, make_response, request, session

app = Flask(__name__)


# 返回模板
@app.route('/')
def index():
    # 模板直接返回参数
    # my_str = 'ryan'
    # my_int = 123
    # return render_template('index.html', my_str=my_str, my_int=my_int)

    # 模板字典返回参数的第一种格式
    # data = {
    #     'my_str': 'ryan',
    #     'my_int': 123
    # }

    # 模板字典返回参数的第二种格式
    data = dict(my_str='ryan', my_int=123)
    return render_template('index.html', **data)


# 重定向
@app.route('/test')
def test():
    return redirect('https://www.baidu.com')


# 返回 Json，推荐用这种方式返回
@app.route('/return')
def return_json():
    json_dict = {
        'username': 'ryan',
        'password': 'a12345'
    }
    return jsonify(json_dict)


# 自定义状态码
# （1）元祖返回
@app.route('/demo4')
def demo4():
    # return '状态码为 666', 666
    # return '状态码为 666', 666, [('Itcast', 'Python')]
    return '状态码为 666', 666, {'Itcast': 'Python'}


# make_response方式
@app.route('/demo5')
def demo5():
    resp = make_response('make response测试')
    resp.headers["Itcast"] = "Python"
    resp.status = "404 not found"  # make_response方式需要填写完整 status code
    return resp


# 设置 cookie
@app.route('/cookie')
def set_cookie():
    resp = make_response('set cookie ok')
    resp.set_cookie('username', 'Ryan', max_age=3600)  # max_age 用于设置过期时间
    return resp


# 读取 cookie
@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


# 删除 cookie
@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('hello world')
    response.delete_cookie('username')
    return response


# 设置 session
# 设置 session 时需要先设置 SECRET_KEY
# 类方法设置 SECRET_KEY
# class DefaultConfig(object):
#     SECRET_KEY = 's1dff1d12hg23fh1jjh'
#
#
# app.config.from_object(DefaultConfig)

# 或者直接设置
app.secret_key = 'fds123af345das44fds'


# 设置 session
@app.route('/set_session')
def set_session():
    session['username'] = 'Ryan'
    return 'set session ok'


# 读取 session
@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)


# 删除 session
@app.route('/delete_session')
def delete_session():
    session.pop('username')
    username = session.get('username')
    return 'get session username {}'.format(username)


if __name__ == '__main__':
    app.run(debug=True)
