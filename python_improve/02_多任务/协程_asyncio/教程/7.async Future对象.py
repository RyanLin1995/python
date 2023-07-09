# A Future is a special low-level awaitable object that represents an eventual result of an
# asynchronous operation.
# Task 继承 Future，Task 对象内部 await 结果的处理基于 Future 对象来的。
# Task 与 Future 区别：当函数 await 状态时，需要获取到函数的返回值才停止，不然事件循环一直进行。Task 对象会自动返回结果，
# 因此可以切换任务。但 Future 对象不会。需要自己添加。但实际上不很少会用到底层的 Future 对象
import asyncio


# 示例一
# async def main():
#     # 获取当前事件循环
#     loop = asyncio.get_running_loop()
#     # 创建一个任务（Future对象），这个任务什么都不干。
#     fut = loop.create_future()
#     # 等待任务最终结果（Future对象），没有结果则会一直等下去。
#     await fut

# 示例二
async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务（Future对象），没绑定任何行为，则这个任务永远不知道什么时候结束。
    fut = loop.create_future()
    # 创建一个任务（Task对象），绑定了set_after函数，函数内部在2s之后，会给fut赋值。即手动设置future任务的最终结果，那么fut就可以结束了。
    await loop.create_task(set_after(fut))
    # 等待Future对象获取最终结果，否则一直等下去
    data = await fut
    print(data)


asyncio.run(main())
