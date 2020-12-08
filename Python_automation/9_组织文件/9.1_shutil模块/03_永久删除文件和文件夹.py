import os
import shutil
import send2trash

# 可以使用 os.unlink(), os.rmdir()，shutil.rmtree() 以及第三方模块 send2trash() 删除文件或文件夹


# 1. os.unlink() 仅用于删除文件
# 创建测试文件
os.makedirs(r"./src")
os.makedirs(r"./test_folder")
shutil.copy(r'./test', r'./test_folder/test.txt')

for file in os.listdir(r"./test_folder"):
    if file.endswith("txt"):
        os.unlink(r"./test_folder/{}".format(file))

# 2. os.rmdir() 仅删除空文件夹
# 创建测试文件
# os.makedirs(r"./test_folder")
os.rmdir(r"./test_folder")
# os.rmdir(r"./src")

# 3. shutil.rmtree() 可以递归删除文件夹
shutil.rmtree(r'./src')

# 4. send2trash() 可以把被删除的文件发送到垃圾箱而不是直接删除
send2trash.send2trash(r'./test')