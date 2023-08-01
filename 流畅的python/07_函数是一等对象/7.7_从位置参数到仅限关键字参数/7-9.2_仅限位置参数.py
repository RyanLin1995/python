def test_divmod1(a, b, /):  # 添加了 / 之后，函数只能使用位置参数而不能使用关键字参数
    return a // b, a % b


print(test_divmod1(10, 12))
print(test_divmod1(a=10, b=12))
