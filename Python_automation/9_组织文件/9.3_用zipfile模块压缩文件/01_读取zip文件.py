# 可以使用 zipfile.ZipFile() 函数读取 zip 文件里面的内容
import zipfile

# 创建一个 ZipFile 对象
exampleFile = zipfile.ZipFile(r'8_backup.zip')

# 获取 zip 文件的内容
print(exampleFile.namelist())

# 获取某个文件的信息
spamInfo = exampleFile.getinfo(r'8_backup/test')
print(spamInfo)
print(spamInfo.file_size)
print(spamInfo.compress_size)
print("Compressed file is {}x smaller!".format(round(spamInfo.file_size/spamInfo.compress_size, 2)))

# 关闭文件
exampleFile.close()


