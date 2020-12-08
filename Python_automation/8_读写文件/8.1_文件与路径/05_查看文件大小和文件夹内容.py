import os


# 可以使用 os.path.getsize() 获取 path 中文件的字节数
print(os.path.getsize(r"/8_读写文件"))  # 只是获取这个文件夹的字节数，不是文件夹里面所有文件的总字节数

# 可以使用 os.listdir() 列出文件夹中所有的文件
print(os.listdir(r"/8_读写文件"))

# 计算文件夹中所有文件的总字节数
total = 0
for file in os.listdir(r"/8_读写文件"):
    total = total + os.path.getsize(os.path.join(r"/8_读写文件", file))
print(total)