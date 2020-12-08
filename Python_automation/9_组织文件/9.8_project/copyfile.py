import re
import os
import shutil


def copy_file(path):
    regex = re.compile(r'(.*)?\.(txt|py)')

    for folder_name, sub_folder_name, file_name in os.walk(path):

        path = os.path.abspath(path)

        result = regex.search(str(file_name))

        if result.group():

            for file in file_name:
                sor_path = os.path.join(folder_name, file)
                dest_path = r"./"
                shutil.copy(sor_path, dest_path)


copy_file(r"/home/ryan/python/Python_automation/8_读写文件/8.4随机生成考卷")


