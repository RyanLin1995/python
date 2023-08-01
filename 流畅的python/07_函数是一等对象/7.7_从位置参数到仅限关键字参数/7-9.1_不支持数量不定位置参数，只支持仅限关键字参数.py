def f(a, *, b):
    return a, b


print(f(1, b=3))
print(f(1, 2, 3, 4, 5))  # 由于存在仅限关键字参数，所以其他参数为意外实参
