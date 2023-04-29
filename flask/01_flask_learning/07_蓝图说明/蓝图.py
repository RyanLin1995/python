from flask import Flask, Blueprint

app = Flask(__name__)

# 创建一个蓝图
user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def get_user():
    return 'user'


# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/profile')

# 注册目录蓝图
# 导入目录蓝图
from flask_goods import goods_bp

app.register_blueprint(goods_bp)

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
