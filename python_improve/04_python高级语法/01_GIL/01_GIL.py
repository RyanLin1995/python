# GIL(全局解析锁)
# 在 Python 中通过 CPython 解析多线程代码时所需要用到的代码，其实际作用是在进程执行过程中，先获取 GIL 确保程序同一时间只有一个线程在执行代码(因为线程共享全局变量)
#
# GIL面试题如下
# 问: 描述Python GIL的概念， 以及它对python多线程的影响？
# 答: 实际上 GIL 和 Python 语言没有关系，是与 Python 语言的解析器有关系。
# Python 语言的解析器有 C语言解析器 ---> Cpython 跟 Java语言解析器 ---> JPython
# 其中只有 Cpython 因为历史原因需要用到 GIL。Python 语言创始人Guido曾经试过移除 GIL，但是效果不明显，因此他建议要在 Python 下进行多任务，请使用多进程
# 详细可试运行 GIL_test 中的多线程测试，会发现 CPU 多核资源没被占满，出现了假的多线程


# 编写一个多线程抓取网页的程序，并阐明多线程抓取程序是否可比单线程性能有提升，并解释原因。
# 多线程的快。因为抓取网页的程序是属于 I/O 密集型(需要调用 receive 或 time.sleep 等，会有堵塞的)的程序，。如果是计算密集型的，不适用 Python 的多线程
# 计算密集型多线程解决方法:1. 切换解析器； 2. 调用其他语句作为多线程

# GIL 与 互斥锁的区别
# 互斥锁是确保资源同一时间只被一个线程所占用，等线程执行完才解锁
# GIL 是确保同一时间只执行一个线程，该线程执行时间可能很短，不一定是执行完了才解开

# 目前常用的Python多线程/多进程方法是多进程+协程

from ctypes import *
from threading import Thread

# 加载 c 动态库

lib = cdll.LoadLibrary("./libloop.so")

t1 = Thread(target=lib.DeadLoop)
t1.start()


# 主线程
while True:
    pass