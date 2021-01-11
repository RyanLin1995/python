# 设置带有参数的装饰器，需要在装饰器中传递参数，然后把装饰器作为一个函数的闭包。参数传递到闭包中且该函数返回值为装饰器

def set_parameter(level_num):  # 如下所说。因此，这里设置了一个闭包，把装饰器作为返回值
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("权限验证1")
            if level_num == 2:
                print("权限验证2")
            func(*args, **kwargs)

        return call_func
    return set_func


@set_parameter(1)  # set_parameter(1) 命令实际上执行了两个步骤，1.调用 set_func
# 并且将参数作为实参传递；2.用上一步的返回值作为装饰器对 test(1) 函数进行装饰
def test1():
    print("----test1----")


@set_parameter(2)
def test2():
    print("----test2----")


test1()
test2()