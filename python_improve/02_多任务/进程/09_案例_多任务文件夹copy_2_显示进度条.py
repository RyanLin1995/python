import os
import time
from multiprocessing import Pool, Manager


def copy_file(file, sou_folder_name, des_folder_name, queue):
    """文件复制"""
    sou_f = open("{}/{}".format(sou_folder_name, file), 'rb')
    content = sou_f.read()
    sou_f.close()

    tar_f = open("{}/{}".format(des_folder_name, file), 'wb')
    tar_f.write(content)
    tar_f.close()

    # 如果拷贝完文件，向队列写入文件名
    queue.put(file)


def main():
    # 1. 获取用户要copy的文件夹名字
    sou_folder_name = input("请输入要copy的文件夹的名字: ")

    # 2. 创建一个新的文件夹
    try:
        des_folder_name = "{}[复件]".format(sou_folder_name)
        os.mkdir(des_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有待copy的文件名字
    file_lists = os.listdir(sou_folder_name)

    # 4. 创建进程池
    po = Pool(3)

    # 5. 创建队列
    queue = Manager().Queue()  # 如果使用进程池，需要采用Manager类里面的Queue方法创建队列

    # 6. 先进程池中添加copy文件
    for file in file_lists:
        po.apply_async(copy_file, args=(file, sou_folder_name, des_folder_name, queue))

    po.close()
    # po.join()
    file_new_lists = []
    all_file_number = len(file_lists)
    count = 0
    while True:
        start = time.time()
        file_name = queue.get()
        count += 1
        # if file_name in file_lists:
        #     file_new_lists.append(file_name)
        # if len(file_new_lists) == len(file_lists):
        #     end = time.time()
        #     print(end - start)
        #     break
        print("\r进度为　{:.2f}%".format((count/all_file_number)*100), end="")
        if count == all_file_number:
            end = time.time()
            print("\n{:.2f}s".format(end - start))
            break

    print()


if __name__ == '__main__':
    main()