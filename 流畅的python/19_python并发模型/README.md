# 进程、线程和声名狼藉的Python GlIL

下面分 10 点说明这些概念在 Python 编程中的应用。

1. Python 解释器的每个实例是一个进程。使用 multiprocessing 或 concurrent.futures 库可以启动额外的 Python 进程。Python 的 subprocess 库用于启动运行外部程序（不管使用何种语言编写）的进程。
2. Python 解释器仅使用一个线程运行用户的程序和内存垃圾回收程序。使用 threading 或 concurrent.futures 库可以启动额外的 Python 线程。
3. 对对象引用计数和解释器其他内部状态的访问受一个锁的控制，这个锁是“全局解释器锁”（Global Interpreter Lock，GIL）。任意时间点上只有一个 Python 线程可以持有 GIL。这意味着，任意时间点上只有一个线程能执行 Python 代码，与 CPU 核数量无关。
4. 为了防止一个 Python 线程无限期持有 GIL，Python的字节码解释器默认每 5 毫秒暂停当前 Python 线程，释放 GIL。被暂停的线程可以再次尝试获得 GIL，但是如果有其他线程等待，那么操作系统调度程序可能会从中挑选一个线程开展工作。
5. 我们编写的 Pvthon 代码无法控制 GIL。但是，耗时的任务可由内置函数或 C 语言（及其他能在 Pvthon/C API 层级接合的语言）扩展释放 GIL。
6. Pvthon 标准库中发起系统调用点的函数均可释放 GIL。这包括所有执行磁盘I\O、网络I\O 的函数，以及 time.sleep()。NumPy/SciPy 库中很多 CPU 密集型函数，以及 zlib 和bz2 模块中执行压缩和解压操作的函数，也都释放 GIL。
7. 在 Python/C API 层级集成的扩展也可以启动不受 GIL 影响的非 Python 线程。这些不受 GIL 影响的线程无法更改 Python 对象，但是可以读取或写入内存中支持缓冲协议的底层对象，例如 bytearray、array.array 和 NumPy 数组。
8. GIL 对使用 Python 线程进行网络编程的影响相对较小，因为 I/O 函数放 GIL，而且与内存读写相比，网络读写的延迟始终很高。各个单独的线程无论如何都要花费大量时间等待，所以线程可以交错执行，对整体吞吐量不会产生重大影响。正如 David Beazley 所言:“Python 线程非常擅长什么都不做。“
9. 对 GIL 的争用会降低计算密集型 Python 线程的速度。对于这类任务，在单线程中依序执行的代码更简单，速度也更快。
10. 若想在多核上运行 CPU 密集型 Python 代码，必须使用多个 Python 进程
