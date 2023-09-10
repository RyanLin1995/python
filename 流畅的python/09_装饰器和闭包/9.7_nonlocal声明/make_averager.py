def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # count += 1  # count 为自由变量，当自由变量为可变类型时可以对其进行操作。但是一旦自由变量为不可变类型时，即不能更新。
        # 由于 count += 1 是给 count 重新赋值，会隐式创建局部变量 count，这样 count 就不是自由变量，不会保存到闭包中。
        # total += new_value
        nonlocal count, total  # 因此要使用 nonlocal关键字，把变量标记为自由变量，使函数即便为变量赋予新值，闭包中保存的变量值也随之更新
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(15))
