# 使用线程池、进程池实现异步操作时用到的对象

import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor


def func(value):
    time.sleep(1)
    print(value)
    return 123


# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)
# 创建进程池
# pool=ProcessPoolExecutor(max_workers=5)
for i in range(10):
    fut = pool.submit(func, i)
    print(fut)


# 使用场景：可能会存在交叉使用。例如：crm项目 80% 都是基于协程异步编程 + 第三方不支持异步的模块，如 MySQL【利用线程、进程、做异步编程】时就可以用

def func1():
    # 某个耗时操作
    time.sleep(2)
    return "Hello"


async def main():
    loop = asyncio.get_running_loop()
    # 1.Run in the default loop's executor （默认ThreadPoolExecutor)
    # 第一步：内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程去执行 func 函数，并返回一个 concurrent.futures.Future 对象
    # 第二步：调用 asyncio.wrap_future 将 concurrent.futures.Future 对象包装为 asyncio.Future 对象，
    # 因为 concurrent.futures.Future 对象不支持 await 语法，所以需要包装为 asyncio.Future 对象才能使用。
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print('default thread pool', result)
    # 2. Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('custom thread pool', result)
    # 3. Run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, func1)
    #     print('custom process pool', result)


asyncio.run(main())
