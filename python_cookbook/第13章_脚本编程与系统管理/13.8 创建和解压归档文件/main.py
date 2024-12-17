import shutil

# 创建压缩文件
shutil.make_archive('test', 'zip', base_dir='test.txt')

# 解压缩文件
shutil.unpack_archive('test.zip', extract_dir='test')
