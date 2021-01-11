import threading
import time

num = 0


def test1(times):
    global num
    for i in range(times):
        locker.acquire()
        num += 1
        locker.release()
    print("test1 number: {}".format(num))


def test2(times):
    global num
    for i in range(times):
        locker.acquire()
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