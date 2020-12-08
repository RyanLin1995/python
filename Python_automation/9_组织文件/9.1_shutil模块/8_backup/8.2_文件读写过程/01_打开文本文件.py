# 利用 open() 可以读取文本文件。 open 函数第一个参数为文本路径，第二个参数为默认参数，不传递时表示默认以 read 的方式(
# "r")打开文件，可传递"r|w|a|rb|r+"等参数。open 函数返回一个 file 对象

file = open("01_test.txt")
print(file)