# 可以使用 shutil.move(src, dst) 移动文件或文件夹
# 创建测试文件
# import os
# os.makedirs(r'./src')
# os.makedirs(r'./dst')
# os.chdir(r'./src')
# f = open(r'tese.txt', 'w')
# f.write(r"Hello world")
# f.close()
import shutil


# 1. 移动文件但是不更改名字
# shutil.move(r'./src/tese.txt', r'./dst')

# 2. 移动文件并改名
# shutil.move(r'./dst/tese.txt', r'./src/test.txt')

# ! 注意，如果 destination 目录有跟 source 目录同名的文件，会覆盖 destination 的同名文件
# 同时 destination 作为目录时必须存在。
