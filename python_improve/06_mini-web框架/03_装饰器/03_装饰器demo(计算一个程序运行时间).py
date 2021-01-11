import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        end_time = time.time()
        print("all time:{:.2}".format(end_time - start_time))

    return call_func


@set_func
def test1():
    print("----test1----")
    for i in range(1, 102502):
        pass


test1()