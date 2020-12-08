sonnetFile = open("02_sonnet29.txt")

# 当用 open() 函数获得一个 file 对象后，可以使用 read() 或 readlines() 方法读取内容
# 使用 read() 方法读取的内容，会把所有内容返回一个字符串
sonnetFileRead = sonnetFile.read()
print(type(sonnetFileRead))
print(sonnetFileRead)

# !!! 注意，当一个file对象使用了一次 read() 后，因为指针去到了文本文件的最后一行，再调用 read()
# 的话是没有数据返回的，因此需要把指针调到第一行或重新打开文件

# 当使用 readlines() 方法读取的内容，返回的是一个列表
sonnetFile.seek(0, 0)  # 使用 seek 方法把指针调回文本第一行
sonnetFileReadLines = sonnetFile.readlines()
print(type(sonnetFileReadLines))
print(sonnetFileReadLines)