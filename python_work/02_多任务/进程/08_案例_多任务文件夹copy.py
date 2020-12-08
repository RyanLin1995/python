import os
from multiprocessing import Pool


def copy_file(file, sou_folder_name):
    """文件复制"""
    sou_f = open("{}/{}".format(sou_folder_name, file), 'rb')
    content = sou_f.read()
    sou_f.close()

    tar_f = open("{}[复件]/{}".format(sou_folder_name, file), 'wb')
    tar_f.write(content)
    tar_f.close()


def main():
    # 1. 获取用户要copy的文件夹名字
    sou_folder_name = input("请输入要copy的文件夹的名字: ")

    # 2. 创建一个新的文件夹
    try:
        os.mkdir("{}[复件]".format(sou_folder_name))
    except:
        pass

    # 3. 获取文件夹的所有待copy的文件名字
    file_lists = os.listdir(sou_folder_name)

    # 4. 创建进程池
    po = Pool(3)

    # 5. 先进程池中添加copy文件
    for file in file_lists:
        po.apply_async(copy_file, args=(file, sou_folder_name))

    po.close()
    po.join()


if __name__ == '__main__':
    main()