#!/usr/bin/env python3

"""
proc_pool.py: a version of the proc.py example from chapter 20,
but using `concurrent.futures.ProcessPoolExecutor`.
"""

# tag::PRIMES_POOL[]
import sys
from concurrent import futures
from time import perf_counter
from typing import NamedTuple

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    flag: bool
    elapsed: float


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def main() -> None:
    if len(sys.argv) < 2:
        workers = None  # 未提供参数时，不自己决定 workers 数量，由 ProcessPoolExecutor 决定
    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(workers)  # 先构建 ProcessPoolExecutor 实例
    actual_workers = executor._max_workers  # type: ignore  # _max_workers 是 ProcessPoolExecutor 的实例属性

    print(f'Checking {len(NUMBERS)} numbers with {actual_workers} processes:')

    t0 = perf_counter()

    numbers = sorted(NUMBERS, reverse=True)  # 倒序排列
    with executor:  # 使用 executor 作为上下文管理器
        for n, prime, elapsed in executor.map(check, numbers):  # executor.map 返回 check 返回的 PrimeResult 实例
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')

    time = perf_counter() - t0
    print(f'Total time: {time:.2f}s')


if __name__ == '__main__':
    main()  # 为什么显示了第一个数字后，程序会卡住，是因为第一个数字检测快，第二个数字检测时间较长，在等待这个数字检测。在这过程中其他数字也在检测。所以第二个检测完其他都检测完，就立即显示出来了
# end::PRIMES_POOL[]
