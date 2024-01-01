"""
Experiment with ``ThreadPoolExecutor.map``
"""
from concurrent import futures
# tag::EXECUTOR_MAP[]
from time import sleep, strftime


def display(*args):  # 把传入的参数打印出来
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):  # 函数在开始时显示一个消息，然后休眠 n 秒后，在结束时也显示一个消息，消息用制表符缩进，缩进数量由 n 决定
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10  # 返回 n * 10 方便收集结果


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # 创建 ThreadPoolExecutor ，有三个线程
    results = executor.map(loiter, range(5))  # 把 5 个任务交给 executor。由于只有三个线程，所以只有三个任务是立即开始的，这三个任务都是非阻塞调用
    display('results:', results)  # 显示 executor.map 的结果，结果是一个生成器
    display('Waiting for individual results:')
    for i, result in enumerate(
            results):  # for 循环中的 enumerate 函数隐式调用 next(results)，这个函数又在(内部)表示第一个任务 (loiter(0))的 future 对象 f 上调用_f.result()。result 方法会阻塞，直到 future 对象运行结束，因此这个循环每次迭代都要等待下一个结果做好准备
        display(f'result {i}: {result}')


if __name__ == '__main__':
    main()
# end::EXECUTOR_MAP[]
