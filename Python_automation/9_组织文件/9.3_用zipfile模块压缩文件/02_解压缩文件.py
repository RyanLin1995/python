import zipfile
import shutil


# 1. 可以使用 ZipFile 对象的 extractall() 方法从压缩文件中解压缩所有文件和文件夹
# shutil.rmtree(r"8_backup")
# exampleFile = zipfile.ZipFile(r'8_backup.zip')
# exampleFile.extractall()  # 不传入任何参数，则会解压到当前目录
# exampleFile.extractall('test')  # 传入参数，则解压到指定文件夹，如果文件夹不存在，则会自动创建
# exampleFile.close()


# 2. 可以使用 ZipFile 对象的 extract() 方法解压缩单个文件，前提是文件在 namelist() 中
exampleFile = zipfile.ZipFile(r'8_backup.zip')
targetFile = exampleFile.namelist()[-1]
print(targetFile)
exampleFile.extract(targetFile)
exampleFile.extract(targetFile, 'test2')  # 传入的第二个参数为指定解压路径，当路径不存在时会自动创建
exampleFile.close()