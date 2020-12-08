import shutil

# 可以使用 shutil.copy(source, destination) 复制文件。其中如果 destination
# 为文件名，则被作为新文件的文件名，如果是文件夹，则保留原文件名作为新文件名
shutil.copy('../../8_读写文件/test', '.')
shutil.copy('../../8_读写文件/test', 'test2')

# 与 shutil.copyfile(source, destination) 区别: shutil.copyfile 的 dst 仅为文件，而 shutil.copy() 的 dst 可以是文件或目录

# 也可以使用 shutil.copytree(source, destination) 复制整个文件夹(包括子文件夹)
shutil.copytree('../../8_读写文件', '8_backup')

