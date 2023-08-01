from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')  # methodcaller 创建的函数会在对象上调用参数指定的方法
print(upcase(s))  # 等价于 str.upper(s)
hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s))
