# spinner_prime_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

import itertools
from multiprocessing import Process, Event
from multiprocessing import synchronize

from primes import is_prime


def spin(msg: str, done: synchronize.Event) -> None:
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
    spinner = Process(target=spin,
                      args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = check(n)  # 进程版将 time.sleep(3) 换成 is_prime(n)。因为两个进程相互独立，所以光标还是会旋转
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
