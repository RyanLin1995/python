import json

from flask import Flask

app = Flask(__name__)


# 定义视图
@app.route('/')
def index():
    """
        返回所有视图网址
    @return:
    """
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})


if __name__ == '__main__':
    app.run(debug=True)
