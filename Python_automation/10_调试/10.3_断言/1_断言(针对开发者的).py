# 先假定 a = 1
a = 1

# 利用 assert 进行断言，断言格式为
# assert 变量名 条件 , 条件为 False 时提示的语句
assert a == 1, "a should be 1."

# 再设置 a = 2
a = 2

# 测试断言
assert a == 1, "a should be 1."
