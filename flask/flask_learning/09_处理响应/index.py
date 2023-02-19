from flask import Flask, render_template, redirect, jsonify

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


if __name__ == '__main__':
    app.run(debug=True)
