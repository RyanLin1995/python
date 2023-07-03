# Task用于在事件循环中添加多个任务

# Tasks用于并发调度协程，通过 asyncio.create_task(协程对象) 的方式创建Task对象，这样可以让协程加入事件
# 循环中等待被调度执行。除了使用asyncio.create_taskO函数以外，还可以用低层级的
# loop.create_task() 或 ensure_future() 函数。不建议手动实例化Task对象。

# 注意：asyncio.create_taskO函数在Python3.7中被加入。在Python3.7之前，可以改用低层级的 asyncio.ensure_future()函数。


import asyncio


# 示例一
# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return "返回值"
#
#
# async def main():
#     print("main开始")
#
#     # 创建Task对象，将当前执行func函数任务添加到事件循环。
#     task1 = asyncio.create_task(func())
#     # 创建Task对象，将当前执行func函数任务添加到事件循环。
#     task2 = asyncio.create_task(func())
#     print("main结束")
#
#     # 当执行某协程遇到O操作时，会自动化切换执行其他任务。
#     # 此处的await是等待相对应的协程全都执行完毕并获取结果
#     retl = await task1
#     ret2 = await task2
#     print(retl, ret2)

# 示例二
async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


# 记住，在协程函数中，事件循环已经创建
async def main():
    print("main开始")

    task = [asyncio.create_task(func(), name='n1'),  # name 为任务名称
            asyncio.create_task(func(), name='n2')]
    print("main结束")

    done, pending = await asyncio.wait(task, timeout=2)  # 指定 timeout (float 或 int 类型) 则它将被用于控制返回之前等待的最长秒数

    print(done)
    print(pending)


# 下边的代码是在运行协程函数前不在协程函数中创建事件循环用
# task_list = [
#     func(),
#     func(), ]
# done, pending = asyncio.run(asyncio.wait(task_list))
# print(done)

asyncio.run(main())
