# 写入文件的方法有两种，一种为 w(覆写)，另一种为 a(追加)。当写入的文件不存在时，调用open()函数，会自动创建文件

# 1. 利用 w(覆写) 进行文件写入
baconFile = open("03_bacon.txt","w")
baconFile.write("Hello world\n")  # 注意，写入文件时如果想换行，需要自己添加换行符
baconFile.close()  # 如果需要在同一个程序中多次打开同一文件，需要先关闭才能重新打开(或者一直不关)

# 2. 使用 a(追加) 进行文件写入
baconFile = open("03_bacon.txt", "a")
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

# 3. 默认方式打开 bacon.txt 文件查看内容
baconFile = open("03_bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)
