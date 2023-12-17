#!/usr/bin/env python3

"""
procs.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.
"""

# tag::PRIMES_PROC_TOP[]
import sys
from multiprocessing import Process, SimpleQueue, cpu_count  # SimpleQueue 用于构建队列
from multiprocessing import queues  # 用于类型提示
from time import perf_counter
from typing import NamedTuple

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]  # 为 SimpleQueue 创建一个类型别名，main 函数发送给这个进程处理的数就是这个类型
ResultQueue = queues.SimpleQueue[PrimeResult]  # 为 SimpleQueue 再创建一个类型别名，main 函数收集的结果是这个类型。队列中的值是 一个元组，由做检测的数和结果构成


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:  # worker 有两个队列，一个存放要检查的数，一个存放结果
    while n := jobs.get():  # 这里使用了 0 作为 “毒药丸”，即职程结束的信号。如果 n 不是 0，则继续循环（一般作为哨符的有 0 和 None）
        print(f'正在处理：{n}\n')
        results.put(check(n))  # 调用检测函数，结果放入到 results 队列
    results.put(PrimeResult(0, False, 0.0))  # 返回一个 PrimeResult(0, False, 0.0) 让主程序知道职程结束


def start_jobs(
        procs: int, jobs: JobQueue, results: ResultQueue  # proces 是并行检测素数的进程数量
) -> None:
    for n in NUMBERS:
        jobs.put(n)  # 把要检查的数放入 jobs 队列
    for _ in range(procs):
        proc = Process(target=worker,
                       args=(jobs, results))  # 为每一个职程派生一个子进程。每个子进程都有各自的 worker 函数，单独运行其中的循环，直到从 jobs 队列中获取 0
        proc.start()  # 启动各个子进程
        jobs.put(0)  # 在各个子进程中添加 0，终止进程

        # 这里没有使用 proc.join() 等待进程结束，一直在 for 循环可以理解为将 jobs 进行切片，每个子进程都从 jobs 中获取要处理的值，但是获取了的不会再存在于 jobs 中


# end::PRIMES_PROC_TOP[]

# tag::PRIMES_PROC_MAIN[]
def main() -> None:
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)  # 启动 proc 进程，处理 jobs 中的作业，结果放入 results
    checked = report(procs, results)  # 获取并显示结果
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')


def report(procs: int, results: ResultQueue) -> int:  # 参数是 proces 的数量和存放结果的队列
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n, prime, elapsed = results.get()  # 获取一个 PrimeResult
        if n == 0:  # 如果等于 0 ，说明一个进程退出了，递增 proces_done 计数
            procs_done += 1
        else:
            checked += 1  # 否则，递增 checked 计数，并显示结果
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


if __name__ == '__main__':
    main()
# end::PRIMES_PROC_MAIN[]
