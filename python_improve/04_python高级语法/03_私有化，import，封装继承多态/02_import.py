# 关于 import 的使用方法有如下:
# from xxx import yyy
# import xxx
# from xxx import *
# import xxx as yyy
# import xxx, yyy
# from xxx import yyy, zzz
# 当使用 import 导入模块时，先找到这个模块的位置，然后导入到解析器，再在当前模块中定义一个变量指向改加载的模块

# 1. 模块搜索路径和改变搜索路径优先级
# 可以使用 sys.path 查询模块搜索路径
import sys

print(sys.path)

# 可以使用 append 或 insert 改变搜索路劲列表，使搜索路径优先级更改
sys.path.append("/lib")  # 添加到列表末尾
print(sys.path)
sys.path.insert(0, "/etc")  # 添加到列表开头
print(sys.path)

# 2. 利用 reload 重新加载模块(请在 ipython 下进行)
# 先把 a.py 导入到本程序
import a

a.tset()
# 修改 a.py 从 print("test") 为 print("test1")
# 先用 import 重新导入 a ，再使用函数 a.test() 发现没有变化
import a

a.tset()
# from importlib import reload，对 a 进行重新加载，发现test()方法跟新修改的一致
from importlib import reload
reload(a)
a.tset()

# ！reload() 只能重新加载通过 import 导入的模块，如果是 form xxx import xxx 的模块是无法reload()的，详细请参考help(reload)
help(reload)
