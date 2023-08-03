# 当不确定一个函数或类的方法需要传递多少个形参时，可以加上 *args 跟 **kwargs *args 代表元祖，××kwargs代表字典。
# 在函数中传入方式为函数名(11, 22, 33, 变量名=参数)，得 args = (11, 22, 33), kwargs = {变量名:参数}
# 而类方法中传入的方式为类名.方法(11, 22, 33, 变量名=参数)，得 类名.args = (11, 22, 33), 类名.kwargs =
# {变量名:参数}

def test2(a, b, *args, **kwargs):
    print("---------")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):  # 这里的 *args 跟 **kwargs 相当于可以接收多个值，以元祖和字典保存
    print(a)
    print(b)
    print(args)
    print(kwargs)

    # test2(a, b, args, kwargs)  # 如果只是把 args 跟 kwagrs 传入 test2，相当于test2(11,
    # 22, (33, 44, 55),{name:"xiaoming",age:18})

    # 正确传入方式
    test2(a, b, *args, **kwargs)  # 相当于 test2(11, 22, 33, 44, 55,
    # name="xiaoming", age=18)。这里的 *args 跟 **kwargs 相当于把原本的 args 跟 kwargs
    # 拆包成与 *args 跟 **kwargs 对应的值


test1(11, 22, 33, 44, 55, name="xiaoming", age=18)

