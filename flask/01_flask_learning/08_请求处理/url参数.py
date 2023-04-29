from flask import Flask
from werkzeug.routing import BaseConverter  # 导入基础转换器类

app = Flask(__name__)


# Flask不同于Django直接在定义路由时编写正则表达式的方式，而是采用转换器语法
# 此处的<>是一个转换器，默认为字符串类型，即将该位置的数据以字符串格式进行匹配、并以字符串为数据类型类型、 user_id为参数名传入视图
# @app.route('/users/<user_id>')

# Flask也提供其他类型的转换器
# DEFAULT_CONVERTERS = {
#     'default':          UnicodeConverter,
#     'string':           UnicodeConverter,
#     'any':              AnyConverter,
#     'path':             PathConverter,
#     'int':              IntegerConverter,
#     'float':            FloatConverter,
#     'uuid':             UUIDConverter,
# }
@app.route('/users/<int:user_id>')
def get_users_id(user_id):
    print(type(user_id))
    return str(user_id)


class MobileConverter(BaseConverter):
    """
        自定义转换器
    """
    regex = r'1[3-9]\d{9}'


# 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: mobile
app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms/<mobile:mob_num>')
def get_users_mob(mob_num):
    print(type(mob_num))
    return str(mob_num)


if __name__ == '__main__':
    app.run(debug=True)
