# shelve 模块可以把 Python 中的变量保存到二进制的 shelf 文件中。
# shelf 文件与Python中的字典相像，由键值对组成，有 keys() 和 values() 方法
# 在 Windows 和 Linux 下，shelf 文件后续为 .bak ， .dat 与 .dir 三者组成
# 在 Mac 下，shelf 后续名为 .db

# 保存变量到 shelf 文件
import shelve
# shelveFile = shelve.open("01_shelve_test")
# cats = ["Zophie", "Pooka", "Simon"]
# shelveFile["cats"] = cats
# shelveFile.close()

# 读取 shelf 文件
shelveFile = shelve.open("01_shelve_test")
ret = shelveFile['cats']
print(ret)
print(list(shelveFile.keys()))
print(list(shelveFile.values()))
