import os

# 利用 os.path.exists(path) 可以检查 path 是否为文件或文件夹
print(os.path.exists(""))
print(os.path.exists(".07_test.py"))

print("------------")

# 利用 os.path.isfile(path) 检查 path 是否为文件
print(os.path.isfile("06_检查路径有效性.py"))
print(os.path.isfile(""))

print("------------")

# 利用 os.path.isfir(path) 检查 path 是否为文件夹
print(os.path.isdir(""))
print(os.path.isdir("06_检查路径有效性.py"))

# 假如想检查是否有在 Linux 下挂载光盘，可用
print(os.path.isdir("/dev/sr0"))  # path 填入磁盘或光盘的路径名称(如: /dev/sr0 或 D:\\) 即可