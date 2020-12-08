import os

# 可以调用 os.path.abspath() 方法，将相对路径转为绝对路径
print(os.path.abspath(r"../8.4随机生成考卷/capitalsquiz1.txt"))

# 可以利用 os.path.isabs() 方法去验证一个路径是否为绝对路径
print(os.path.isabs("../../"))
print(os.path.isabs("/"))

# 可以利用 os.path.relpath(path, start) 方法，将返回从 start 路径到 path 相对路径
print(os.path.relpath("..", r"/home/ryan/python/Python_automation/7_正则表达式"))

# 可以通过 os.path.basename(path) 获取最后一个斜杠后的内容(文件名)；
# 通过 os.path.dirname(path) 获取最后一个斜杠前的内容(路径名)
print(os.path.basename(r"/8_读写文件/8.1_文件与路径/04_绝对路径和相对路径.py"))
print(os.path.dirname(r"/8_读写文件/8.1_文件与路径/04_绝对路径和相对路径.py"))

# 如果同时需要一个路劲的目录名称和基本名称，可以使用 os.path.split() 获得路径名的元祖
calcFilePath = '/home/ryan/python/Python_automation/8_读写文件/04_绝对路径和相对路径.py'
print(os.path.split(calcFilePath))

# 但是 os.path.split 不返回列表，如果需要列表，可以使用 split 方法，传入参数 os.path.sep。
# os.path.sep为文件分割线
print(calcFilePath.split(os.path.sep))  # Linux 跟 Mac 的表头为空

# 同样也可以用 os.path.dirname 跟 os.path.basename 组成元祖
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))