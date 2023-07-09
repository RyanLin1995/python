# uvloop是asyncio的事件循环的替代方案。其事件循环>默认asyncio的事件循环。
import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())  # 设置 asyncio 事件循环为 uvloop
# 编写asyncio的代码，与之前写的代码一致。
# 内部的事件循环自动化会变为uv1oop
asyncio.run(...)
