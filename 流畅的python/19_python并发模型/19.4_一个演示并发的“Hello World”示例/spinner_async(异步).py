# 线程和进程由操作系统调度程序分配 CPU 时间驱动。相比之下，协程由应用级事件循环驱动:事件循环管理待定协程队列，逐个驱动，监视由协程发起的 IO
# 操作触发的事件在各个事件发生时把控制权传回相应的协程。事件循环、库协程以及用户协程都在同一个线程中执行。
# 因此，在协程中花费的任何时间都会减慢事件循环，以及所有其他协程。

# spinner_async.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_ASYNC_TOP[]
import asyncio
import itertools


async def spin(msg: str) -> None:  # 这里不需要通过 Event 信号指明 slow 工作已经做完
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)  # 使用 await asyncio.sleep(.1) 代替 time.sleep(.1)，暂停时不阻塞其他协程
        except asyncio.CancelledError:  # 捕捉到 CancelledError 就退出
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow() -> int:
    await asyncio.sleep(3)  # 同样使用 await asyncio.sleep() 代替 time.sleep()
    return 42


# end::SPINNER_ASYNC_TOP[]

# tag::SPINNER_ASYNC_START[]
def main() -> None:  # 唯一的常规函数
    result = asyncio.run(
        supervisor())  # asyncio.run 函数启动事件循环，驱动这个协程，最终也驱动其他协程。main 函数保持阻塞，直到 supervisor 返回值。supervisor 的返回值将变为
    # asyncio.run() 的返回值
    print(f'Answer: {result}')


async def supervisor() -> int:  # 定义协程函数
    spinner = asyncio.create_task(spin('thinking!'))  # asyncio.create_task 调度 spin 最终执行，现在返回的是一个 asyncio.Task 实例
    print(f'spinner object: {spinner}')  # 打印协程对象
    result = await slow()  # await 关键字调用 slow，阻塞 supervisor，直到 slow 返回，slow 返回的值会被赋予到 result
    spinner.cancel()  # Task.cancel 方法在 spin 协程中抛出 CancelledError 异常
    return result


if __name__ == '__main__':
    main()
# end::SPINNER_ASYNC_START[]

# 运行协程的3种主要方式
# asyncio.run(coro())：在常规函数中调用，驱动一个协程对象，通常作为程序中所有异步代码的入口，例如本例中的supervisor。这个调用保持阻塞，一直到 coro的主体返回。run()调用的返回值是 coro 主体的返回值。
# asyncio.create_task(coro())：在协程中调用，调度另一个协程最终执行。这个调用不中止当前协程。返回一个 Task 实例，包装协程对象，提供控制和查询协程状态的方法。
# await coro()：在协程中调用，把控制权转给 coro() 返回的协程对象。中止当前协程，直到 coro 的主体返回。这个异步等待表达式的值是 coro 主体的返回值。
