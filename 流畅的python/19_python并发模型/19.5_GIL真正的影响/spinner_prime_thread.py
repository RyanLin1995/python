# spinner_prime_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import itertools
from threading import Thread, Event

from primes import is_prime


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def check(n: int) -> int:
    return is_prime(n)


def supervisor(n: int) -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    # 线程版将 time.sleep(3) 换成 is_prime(n)，光标依然会转，是因为 Python 每隔 5毫秒(默认值)中止运行线程，其他待定线程可以获得 GIL。所以，运行 is_prime
    # 的主线程每 5毫秒中断一次，次线程复苏，迭代一次 for 循环，直到在 done 事件上调用 wait 方法，释放GIL。随后，主线程再次获得 GIL，is_prime 接着计算 5 毫秒。这对本例没有明显影响，因为 spin
    # 函数迭代一次的速度很快，收到 done 事件后就释放 GIL，所以几乎没有争用 GIL。多数时候，GIL 由运行 is_prime 的主线程持有。但注意，如果有两个或以上线程都想占用大量 CPU 时间，那么程序运行速度要比顺序执行的代码更慢。
    result = check(n)
    done.set()
    spinner.join()
    return result


def main() -> None:
    n = 5_000_111_000_222_021
    result = supervisor(n)
    msg = 'is' if result else 'is not'
    print(f'{n:,} {msg} prime')


if __name__ == '__main__':
    main()
