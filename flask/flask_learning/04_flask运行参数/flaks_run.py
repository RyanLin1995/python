from flask import Flask

app = Flask(__name__)


# 定义视图
@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # 运行 flask 提供的调试服务器
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run()
