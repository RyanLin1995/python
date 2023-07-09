import asyncio


# 协程函数，定义函数时候 async def 函数名。
# 协程对象，执行 协程函数() 得到的协程对象。

async def func():
    print("快来搞我吧！")


result = func()  # 注意，执行协程函数创建的是协程对象，而不会执行函数内部的代码

# 运行异步
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)  # 如果想要运行协程函数内部代码，必须要将协程对象交给事件循环来处理

# 运行异步简便写法
asyncio.run(result)  # 等价于 asyncio.run(func())
