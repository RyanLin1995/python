import threading
import time

num = 0


def test1(times):
    global num
    # 上锁，如果之前没有上锁，那么上锁成功。如果之前上锁了，代码运行到这一步会被堵塞，直到锁被解开
    locker.acquire()
    for i in range(times):
        num += 1
    # 解锁
    locker.release()
    print("test1 number: {}".format(num))


def test2(times):
    global num
    locker.acquire()
    for i in range(times):
        num += 1
    locker.release()
    print("test2 number: {}".format(num))


locker = threading.Lock()


def main():

    t1 = threading.Thread(target=test1, args=(300000,))

    t2 = threading.Thread(target=test2, args=(300000,))

    t1.start()
    t2.start()

    time.sleep(1)

    print("Global number: {}".format(num))


if __name__ == '__main__':
    main()