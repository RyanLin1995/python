from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from unicodedata import name

from charindex import InvertedIndex

STATIC_PATH = Path(__file__).parent.absolute() / 'static'  # 使用 pathlib 拼接路径更优雅，因为重载了 / 运算符

app = FastAPI(  # 初始化 app
    title='Mojifinder Web',
    description='Search for Unicode characters by name.',
)


class CharName(BaseModel):  # JSON 响应的 pydantic 模式，有两个字段
    char: str
    name: str


def init(app):  # 构建 index，加载静态 HTML 表单，两者都依附在 app.state 上，供后面使用
    app.state.index = InvertedIndex()
    app.state.form = (STATIC_PATH / 'form.html').read_text()


init(app)  # 服务器加载这个模块时 运行 init


@app.get('/search', response_model=list[CharName])  # /search 路径的路由。response_model是前面的 CharName 构成的列表
async def search(q: str):  # q 是 HTTP 查询字符串，即 /search?q=。q 不能为空
    chars = sorted(app.state.index.search(q))
    return ({'char': c, 'name': name(c)} for c in chars)  # 返回由字典构成的可迭代对象，与 response_model 兼容


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def form():  # 常规函数，用于生成响应
    return app.state.form

# no main funcion  # 没有主函数，由 uvicron 加载和驱动
