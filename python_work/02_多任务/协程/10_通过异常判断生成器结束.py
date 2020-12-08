def create_num(all_num):
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a
        a, b = b, a + b
        current_num += 1
    return "OK....."


obj2 = create_num(5)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret)  # yield里面调用reture的返回值，是在捕获到的异常里面的值
        # print(ret.value)
        break

