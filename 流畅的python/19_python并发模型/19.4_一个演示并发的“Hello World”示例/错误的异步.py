# spinner_async_experiment.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import asyncio
import itertools
import time


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    print('THIS WILL NEVER BE OUTPUT')


# tag::SPINNER_ASYNC_EXPERIMENT[]
async def slow() -> int:
    time.sleep(3)  # time.sleep(3) 阻塞了 3 秒，程序什么都做不了，因为主线程被阻塞了，而主线程是唯一的线程。操作系统继续其他活动。3 秒后，sleep 不在阻塞，slow 返回
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))  # 创建协程
    print(f'spinner object: {spinner}')
    result = await slow()  # 这个 await 表达式将控制权给 slow 协程
    spinner.cancel()  # slow 一旦返回，spinner 任务就取消。控制流始终没有触及到 spin 协程主体
    return result


# end::SPINNER_ASYNC_EXPERIMENT[]

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
