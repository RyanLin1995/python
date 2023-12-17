# spinner_async_experiment.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import asyncio
import itertools

from primes import is_prime


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    print('THIS WILL NEVER BE OUTPUT')


async def check(n: int) -> int:
    return is_prime(n)


async def supervisor(n: int) -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    result = await check(n)  # 协程版 将 time.sleep(3) 换成 is_prime(n)，光标不旋转，因为主线程被 is_prime(n) 函数阻塞了
    spinner.cancel()
    return result


# end::SPINNER_ASYNC_EXPERIMENT[]

def main() -> None:
    n = 5_000_111_000_222_021
    result = asyncio.run(supervisor(n))
    msg = 'is' if result else 'is not'
    print(f'{n:,} {msg} prime')


if __name__ == '__main__':
    main()
