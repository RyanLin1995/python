# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_THREAD_TOP[]
import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:  # 函数在单独的线程中运行，done 参数的值是一个 threading.Event 实例，一个用于同步线程的简单对象
    for char in itertools.cycle(r'\|/-'):  # 无限循环这四个字符
        status = f'\r{char} {msg}'  # 用文本实现动画的技巧：使用 ASCII 回车符（'\r'）把光标移到行头
        print(status, end='', flush=True)
        if done.wait(.1):  # 如果其他线程设置了这个事件，则 Event.wait(timeout=None) 方法返回 True；经过 timeout 指定时间后，返回 False
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # 显示空格，并把光标移到开头，清空状态行


def slow() -> int:
    time.sleep(3)  # slow() 由主线程调用。因此会阻塞主线程，但是释放了 GIL，所以指针能继续旋转
    return 42


# end::SPINNER_THREAD_TOP[]

# tag::SPINNER_THREAD_REST[]
def supervisor() -> int:
    done = Event()  # threading.Event 实例是协调线程活动的关键
    spinner = Thread(target=spin, args=('thinking!', done))  # 创建一个 Thread 实例
    print(f'spinner object: {spinner}')  # 显示创建的 Thread 实例，状态为<Thread(Thread-1, initial)>，其中 initial 为线程未启动状态
    spinner.start()  # 启动线程
    result = slow()  # 调用 slow() 阻塞主线程，因此子线程运行旋转指针动画
    done.set()  # 等待3秒后，将 Event 标志设置为 True，终止子线程的 for 循环
    spinner.join()  # 等待子线程运行完毕
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
# end::SPINNER_THREAD_REST[]
