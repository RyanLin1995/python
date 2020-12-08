import os

# 可以利用 os.makedirs() 创建新的文件夹，创建时需要可以传入子文件夹
os.makedirs("test1/test1")

# os.mkdir() 只能在当前目录下创建目录，不支持递归创建，但可以在创建时添加权限，默认值为0777
os.mkdir("test2", 0o700)
os.mkdir("./test3/test3", 0o777)