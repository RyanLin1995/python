import gevent
# gevent: python的异步并发库，特点是遇到延迟会切换任务
# 当导入了gevent，需要用到延迟或堵塞的函数时，都要用到gevent里面的延迟函数
# 如 time.sleep ---> gevent.sleep


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.1)  # 因为调用了gevent，因此延迟不能用
        gevent.sleep(0.5)  # gevent里面的延迟函数


print("----1----")
# 创建gevent对象
g1 = gevent.spawn(f, 5)
print("----2----")
g2 = gevent.spawn(f, 5)
print("----3----")
g3 = gevent.spawn(f, 5)
print("----4----")

g1.join()  # 堵塞g1，使g1延迟，这样就会切换到g2
g2.join()
g3.join()