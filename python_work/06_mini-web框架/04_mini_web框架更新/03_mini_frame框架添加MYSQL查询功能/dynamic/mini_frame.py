import re
from pymysql import connect

URL_FUNC_DICT = {}


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route('/index.html')
def index():

    with open("./templates/index.html", encoding='UTF-8') as f:
        content = f.read()
    # my_stock_info = "这是MYSQL查询出来的数据"
    # content = re.sub(r'{%content%}', my_stock_info, content)

    # 一般情况下，前端提供的模板中都会带有数据，通过右键浏览器，选择“检查”可以得知数据是根据哪一行html代码所得的
    # 那么在框架中只需要把从数据库中查找到的数据替换html中的数值即可。本案例中需要替换的是<tr></tr>
    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()
    cur.execute('select * from info;')
    stock_infos = cur.fetchall()
    cur.close()
    con.close()

    tr_template = """<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>
        <input type="button" value="添加" id="toAdd" systemidvalue="000007">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[7])

    content = re.sub(r'{%content%}', html, content)

    return content


@route('/center.html')
def center():

    with open("./templates/center.html", encoding='UTF-8') as f:
        content = f.read()
    # now = time.ctime()
    # my_stock_info = str(now)
    # content = re.sub(r'{%content%}', my_stock_info, content)
    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()
    cur.execute('select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id = f.info_id;')
    stock_infos = cur.fetchall()
    cur.close()
    con.close()

    tr_template = """<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
        </td>
        <td>
            <input type="button" value="删除" id="toDel" systemidvalue="300268">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6])

    content = re.sub(r'{%content%}', html, content)

    return content


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]

    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常:{}".format(ret)


