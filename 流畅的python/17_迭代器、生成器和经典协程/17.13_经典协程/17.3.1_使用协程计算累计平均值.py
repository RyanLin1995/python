from collections.abc import Generator


def averager() -> Generator[
    float, float, None]:  # Generator第一个参数是 YieldType，是 next(it) 调用返回值的类型。第二个参数是 SendType。只有当生成器作为协程时才有意义。第三个参数 ReturnType 也只在注解协程时有意义，因为迭代器不像常规函数那样可以返回值。对于用作迭代器的生成器，唯一合理的操作是调用 next(it)，也可以通过 for循环和其他迭代形式间接调用。
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average  # 每次激活之后，协程在 yield 处暂停，等待发送值。
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()
    print(next(
        coro_avg))  # 调用 next(coro_avg)后，协程向前执行到 yield，产出 average 变量的初始值。另外，也可以调用 coro_avg.send(None) 开始执行协程，这其实就是内置函数 next() 的作用。但是不能发送 None 之外的值，因为协程只能在 yield 处暂停时接受发送的值。调用 next() 或 send(None) 向前执行到第一个 yield 的过程叫作“预激协程”。
    print(coro_avg.send(
        10))  # 激活协程，yield 表达式把得到的值 (10) 赋给 term 变量。循环余下的部分更新 total、count 和 average 这 3 个变量的值。while 循环的下一次选代产出 average 变量的值，协程在 yield 关键字处再一次暂停。
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    coro_avg.close()  # 可以用来终止协程
