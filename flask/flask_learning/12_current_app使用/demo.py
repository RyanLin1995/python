from flask import Flask

app = Flask(__name__)

# 主文件设置 redis-cli 参数
app.redis_cli = 'redis client'


@app.route('/')
def index():
    print(app.redis_cli)
    return app.redis_cli


from current_app_test import bp

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
