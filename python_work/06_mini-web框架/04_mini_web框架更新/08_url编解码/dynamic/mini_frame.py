import re
import urllib.parse
from pymysql import connect

URL_FUNC_DICT = {}


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r'/index.html')
def index(ret):

    with open("./templates/index.html", encoding='UTF-8') as f:
        content = f.read()
    # my_stock_info = "这是MYSQL查询出来的数据"
    # content = re.sub(r'{%content%}', my_stock_info, content)

    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()
    cur.execute('select * from info;')
    stock_infos = cur.fetchall()
    cur.close()
    con.close()

    tr_template = """
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="{}">
        </td>
    </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[7], line_info[1])

    content = re.sub(r'{%content%}', html, content)

    return content


@route(r'/center.html')
def center(ret):

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

    tr_template = """
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/{}.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
        </td>
        <td>
            <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="{}">
        </td>
    </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[0], line_info[0])

    content = re.sub(r'{%content%}', html, content)

    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):

    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()

    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断是否有这个股票代码
    command = 'select * from info where code=%s;'
    cur.execute(command, (stock_code,))
    if not cur.fetchone():
        cur.close()
        con.close()
        return "没有这只股票"

    # 3. 判断是否已关注过这个代码
    command = 'select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;'
    cur.execute(command, (stock_code,))
    if cur.fetchone():
        cur.close()
        con.close()
        return "你已经关注过了"

    # 4. 添加关注
    command = 'insert into focus(info_id) select id from info where code=%s;'  # 这里的focus.info_id与info.id为外键的关系
    cur.execute(command, (stock_code,))
    con.commit()
    cur.close()
    con.close()

    return "关注{}成功".format(str(stock_code))


@route(r"/del/(\d+)\.html")
def del_focus(ret):

    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()

    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 判断是否有这个股票代码
    command = 'select * from info where code=%s;'
    cur.execute(command, (stock_code,))
    if not cur.fetchone():
        cur.close()
        con.close()
        return "没有这只股票"

    # 3. 判断是否已关注过这个代码
    command = 'select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;'
    cur.execute(command, (stock_code,))
    if not cur.fetchone():
        cur.close()
        con.close()
        return "你没有关注过{}".format(str(stock_code))

    # 4. 取消关注
    command = 'delete from focus where info_id = (select id from info where code=%s);'  # 这里的focus.info_id与info.id为外键的关系
    cur.execute(command, (stock_code,))
    con.commit()
    cur.close()
    con.close()

    return "取消关注{}成功".format(str(stock_code))


@route(r'/update/(\d+)\.html')
def show_update_page(ret):

    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 打开模板
    with open("./templates/update.html", encoding='UTF-8') as f:
        content = f.read()

    # 3. 根据股票代码查询相关信息
    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()
    command = 'select note_info from focus where info_id = (select id from info where code=%s);'
    cur.execute(command, (stock_code,))
    stock_infos = cur.fetchone()
    note_info = stock_infos[0]  # 因为SQL代码仅获取了note_info，因此note_info是第一个参数
    cur.close()
    con.close()

    content = re.sub(r'{%code%}', stock_code, content)
    content = re.sub(r'{%note_info%}', note_info, content)

    return content


@route(r'/update/(\d+)/(.*)\.html')
def save_update_page(ret):

    # 1. 获取股票代码和备注信息
    stock_code = ret.group(1)
    comment = ret.group(2)
    comment = urllib.parse.unquote(comment)  # 浏览器在把用户输入的信息传给服务器时会进行URL编码，以防服务器解析错误。
    # 因此在这里要对数据进行解码，然后保存到数据库中。不然的话是直接保存了URL编码后的信息。(浏览器遇到多个空格只显示一个)

    # 2. 更新数据库
    con = connect(host='localhost', user='root', password='a12345', database='stock_db', port=3306, charset='utf8')
    cur = con.cursor()
    command = 'update focus set note_info=%s where info_id=(select id from info where code=%s);'
    cur.execute(command, (comment, stock_code))
    con.commit()
    cur.close()
    con.close()

    return "修改{}备注成功".format(stock_code)


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]

    try:
    #     return URL_FUNC_DICT[file_name]()
    # except Exception as ret:
    #     return "产生了异常:{}".format(ret)
        for url, func in URL_FUNC_DICT.items():
            # {
            #     r'/index.html':index,
            #     r'/center.html':center,
            #     r'/add/\d+\.html':add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)  # 直接传递正则匹配的对象，让函数自行去决定是否使用
        else:
            return "请求的URL({})没有对应函数".format(file_name)
    except Exception as ret:
        return "产生异常: {}".format(str(ret))




