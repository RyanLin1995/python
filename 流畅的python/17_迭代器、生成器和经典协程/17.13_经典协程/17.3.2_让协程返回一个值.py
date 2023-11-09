from collections.abc import Generator
from typing import Union, NamedTuple, TypeAlias


class Result(NamedTuple):
    count: int
    average: float


class Sentinel:
    """
        哨符类
    """

    def __repr__(self):
        return f'<Sentinel>'


STOP = Sentinel()  # 这是一个哨符，用于让协程停止收集数据并发返回结果

SendType: TypeAlias = Union[float, Sentinel]  # 用于 Generator 第二个参数类型


def average2(verbose: bool = False) -> Generator[
    None, SendType, Result]:  # 这个协程产出值为 None，因为它不产出数据。接收数据为 SendType，返回一个元组
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield  # 这个 yield 只存在于协程中，目的是消耗数据。产出 None，从.send(term) 接收 term
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):  # 如果 term 是哨符则跳出
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)  # 跳出循环后返回一直元组


if __name__ == '__main__':
    coro_avg = average2()
    print(next(coro_avg))  # 激活协程
    print(coro_avg.send(10))  # 返回的是 None
    print(coro_avg.send(30))  # 返回的是 None
    print(coro_avg.send(6.5))  # 返回的是 None
    # print(coro_avg.close())  # 仅仅 close 协程并不返回结果
    try:
        coro_avg.send(STOP)
    except StopIteration as exc:
        print(exc.value)  # StopIteration 实例的 value 属性绑定的即为终止的协程的返回值


    # 委托生成器可以直接获取协程的返回值
    def compute():
        res = yield from average2(True)  # yield from 机制在处理表示协程终止的 StopIteration 异常时获取返回值
        print('computed:', res)
        return res


    comp = compute()
    for v in [None, 10, 20, 30, STOP]:
        comp.send(v)
