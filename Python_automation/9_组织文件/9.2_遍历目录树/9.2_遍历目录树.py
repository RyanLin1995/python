# 可以使用 os.walk() 对一个文件夹进行遍历。该函数返回三个值: 当前文件夹，当前文件夹子文件夹以及当前文件夹文件
import os

for folderName, subFolders, files in os.walk(r"../"):
    print("The current folder is {}".format(folderName))

    for subFolder in subFolders:
        print("The sub folder of {} is {}".format(folderName, subFolder))

    for file in files:
        print("The file of {} is {}".format(folderName, file))

    print()