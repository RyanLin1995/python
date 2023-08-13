from array import array

# 内置 memoryview 类是一种共享内存的序列类型，可在不复制字节的情况下处理数组的切片。

octets = array('B', range(6))  # 创建一个6字节数组（类型代码为'B'）
m1 = memoryview(octets)  # 根据数组创建一个 memoryview 对象
print(m1.tolist())
# cast 方法可以改变读写多字节单元的方式，无需位移，返回的是一个 memoryview 对象且始终共享内存
m2 = m1.cast('B', [2, 3])  # 根据前一个 memoryview 对象构建一个新的 2行3列的 memoryview 对象
print(m2.tolist())
m3 = m1.cast('B', [3, 2])  # 在构建一个 3行2列 的memoryview 对象
print(m3.tolist())

m2[1, 1] = 22  # 使用 22 覆盖 m2 上 1行1列 的值
m3[1, 1] = 33  # 同样使用 33 覆盖 m3 上 1行1列 的值

print(octets)  # 原始数组值被更改，证明 octets, m1, m2, m3之间内存共享
