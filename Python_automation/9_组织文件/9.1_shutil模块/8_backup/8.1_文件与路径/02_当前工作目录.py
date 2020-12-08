import os

# 用 os.getcwd() 可以获取当前工作目录
print(os.getcwd())

# 用 os.chdir() 可以改变当前工作目录
os.chdir("../../..")
print(os.getcwd())

# 如果文件夹不存在，则会显示错误
os.chdir("../test")
print(os.getcwd())