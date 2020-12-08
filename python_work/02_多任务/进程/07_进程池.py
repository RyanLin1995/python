import time
import os
import random
from multiprocessing import Pool


def worker(ids):
    t_start = time.time()
    print("{} 开始执行, 进程ID为: {}".format(ids, os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print("{} 运行结束，总执行时间为 {:.2}".format(ids, (t_stop - t_start)))


# 定义一个进程池，最大进程数3
po = Pool(3)
for i in range(10):
    # Pool().apply_async(要调用的目标, (传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程调用目标
    po.apply_async(worker, (i,))

print("---start---")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有子线程执行完毕，必须放在close后面
print("---stop---")