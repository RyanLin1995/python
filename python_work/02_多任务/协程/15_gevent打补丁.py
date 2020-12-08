import time
import gevent
from gevent import monkey
# 当导入了gevent，需要用到延迟或堵塞的函数时，都要用到gevent里面的延迟函数
# 如 time.sleep ---> gevent.sleep
# 但是如果不想改变切换，可以通过打补丁的方式，继续使用原来的延迟或堵塞函数

monkey.patch_all()  # 给程序打上补丁，让程序不需要改变延迟或堵塞函数


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.1)
        # gevent.sleep(0.5)


# print("----1----")
# g1 = gevent.spawn(f, 5)
# print("----2----")
# g2 = gevent.spawn(f, 5)
# print("----3----")
# g3 = gevent.spawn(f, 5)
# print("----4----")

# g1.join()
# g2.join()
# g3.join()

# 可以把所创建的对象放到一个列表里面，然后把列表添加到gevent.joinall里面，即可调用全部对象
gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
])