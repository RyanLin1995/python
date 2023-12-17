# spinner_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_PROC_IMPORTS[]
import itertools
import time
from multiprocessing import Process, Event  # 导入 multiprocessing API
from multiprocessing import synchronize  # 为什么需要导入 synchronize，是因为 multiprocessing.Event 是函数，返回的是 synchronize.Event 实例


def spin(msg: str, done: synchronize.Event) -> None:
    # end::SPINNER_PROC_IMPORTS[]
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42


# tag::SPINNER_PROC_SUPER[]
def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')  # 打印进程对象
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


# end::SPINNER_PROC_SUPER[]

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
