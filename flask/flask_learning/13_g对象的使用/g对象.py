from flask import Flask, g

app = Flask(__name__)


def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id={} user_name={}'.format(user_id, user_name))


@app.route('/')
def get_user_profile():
    g.user_id = 123  # g 对象可以临时保存数据，因此可以作为传参用
    g.user_name = 'ryan'
    db_query()
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
