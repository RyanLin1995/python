import copy

# 通过打印c跟d的内存，发现两者不同，但是打印第一个值的内存，发现内存相同，因此，列表复制[:]为浅拷贝
a = [11, 22]
b = [33, 44]
c = [a, b]
d = c[:]  # 复制列表
print(id(c))
print(id(d))
print(id(c[0]))
print(id(d[0]))

print("----------------------")

# 关于copy字典，因为字典是无序的，而且字典的key是存在字典中，但是value的值是哈希了的，然后字
# 典中只保存了value的哈希值的指向。当使用copy对字典进行浅拷贝时，会发现新的字典跟旧的字典的value是同一指向，
d = dict(name="zhangsan", age=27, children_age=[11, 22])
co = d.copy()
print(id(d))
print(id(co))

d["children_age"].append(9)
print(d)
print(co)

print("----------------------")


# 把列表作为参数进行传递时，是浅拷贝
def test(nums):
    nums.append(3)


nums = [1, 2]

test(nums)
print(nums)

# 如果不行修改源数据，可以使用深拷贝
new_nums = copy.deepcopy(nums)
test(new_nums)
print(new_nums)
print(nums)