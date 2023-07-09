# 什么是异步送代器
# 实现了 __aiter()__ 和 __anext()__ 方法的对象。__anext__ 必须返回一个 awaitable 对象。async for会
# 处理异步选代器的 __anext()__ 方法所返回的可等待对象，直到其引发一个StopAsyncIteration异常。由 PEP492 引入。
# 什么是异步可选代对象？
# 可在async for语句中被使用的对象。必须通过它的 __aiter()__ 方法返回一个 asynchronous iterator。由 PEP492 引入。
import asyncio


class Reader(object):
    """自定义异步选代器群（同时也是异步可选代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    async for item in obj:  # 异步迭代器必须在协程函数中运行
        print(item)


asyncio.run(func())
