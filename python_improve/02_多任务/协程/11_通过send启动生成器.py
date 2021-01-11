def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print("ret--->", ret)
        a, b = b, a + b
        current_num += 1


obj = create_num(10)

# obj.send(None)  # send不能放在第一次调用，除非传的是None

ret = next(obj)
print(ret)

# 通过send启动生成器，send里面的值会传回去给yield a，即send的值 == yield a
ret = obj.send('haha')
print(ret)

