import time


def test1():
    for i in range(50):
        print("----1: {}----".format(i))
        time.sleep(0.1)
        yield


def test2():
    for i in range(50):
        print("----2: {}----".format(i))
        time.sleep(0.1)
        yield


def main():
    t1 = test1()
    t2 = test2()
    # 先让 t1 运行一段时间，当 t1 遇到 yield 时，返回到调用 t1 的地方，然后执行 t2 。同理， t2 遇到yield
    # 后会切换到 t1。 这样 t1/t2/t1/t2 交替运行，实现协程多任务
    while True:
        try:
            next(t1)
            next(t2)
        except:
            break


if __name__ == '__main__':
    main()