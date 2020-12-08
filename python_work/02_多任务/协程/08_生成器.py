# 生成器是一种特殊的迭代器
# 1. 创建生成器的一种方式
# nums = [x * 2 for x in range(10)]  # 列表，占用空间
#
# print(nums)
#
# nums = (x * 2 for x in range(10))  # 返回生成数据的方式，不占用空间
#
# print(nums)
#
# for num in nums:
#     print(num)


# 2. 创建生成器的另一种方式
def create_num(all_num):
    print('----1----')
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        print('----2----')
        # print(a)
        yield a  # 一个函数里面有yield语句，则从函数变为一个生成器的模板(类似于类)
        print('----3----')
        a, b = b, a + b
        current_num += 1
        print('----4----')


# 如果在调用create_num的时候，发现函数中有yield，此时不是调用函数，而是创建一个生成器对象
obj = create_num(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

# num 来源于yield的返回值。
# 当代码运行到yield时将会暂停，把值返回到调用的函数。调用函数运行完毕后模板，指针不会从代码开始执行，而是从yield暂停位置开始执行。
# for num in obj:
#     print(num)
