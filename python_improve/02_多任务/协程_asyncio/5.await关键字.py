# await 一般后面加可等待对象（协程对象、Future、Task对象->IO等待），等等待对象的值得到结果后再继续向下走

import asyncio


# 示例一
# async def func():
#     print("来玩啊")
#     response = await asyncio.sleep(2)
#     print("结束", response)

# 示例二
# async def others():
#     print("start")
#     await asyncio.sleep(2)
#     print("end")
#     return "返回值"
#
#
# async def func():
#     print("执行协程函数内部代码")
#     # 遇到 IO 操作挂起当前协程（任务），等 IO 操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
#     response = await others()
#     print("IO请求结束，结果为", response)

# 示例三
async def others(num):
    print("start", num)
    await asyncio.sleep(2)
    print("end")
    return num


async def func():
    print("执行协程函数内部代码")
    # 遇到 IO 操作挂起当前协程（任务），等 IO 操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response1 = await others(1)
    print("IO请求结束，结果为", response1)

    response2 = await others(2)
    print("IO请求结束，结果为", response2)


asyncio.run(func())
