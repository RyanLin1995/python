# 如果想新建一个 zip file，可以在打开 zipfile 对象时传入写(w)模式
# 如果想追加一个文件到压缩文件夹，可以用追加(a)模式
import zipfile
import os

# 新建一个 new.zip 文件，文件内容为 01 跟 02 的 py 文件
exampleFile = zipfile.ZipFile('new.zip', 'w')
exampleFile.write("02_解压缩文件.py", compress_type=zipfile.ZIP_DEFLATED)
exampleFile.close()

# 追加 01_读取zip文件.py 到 new.zip
exampleFile = zipfile.ZipFile('new.zip', 'a')
exampleFile.write("01_读取zip文件.py", compress_type=zipfile.ZIP_DEFLATED)
exampleFile.close()

# 利用 zipfile, os.walk, os.path.join 添加文件夹
exampleFile = zipfile.ZipFile('new.zip', 'a')

for file_paths, dir_names, file_names in os.walk("test"):
    for file_name in file_names:
        exampleFile.write(os.path.join(file_paths, file_name))

exampleFile.close()
