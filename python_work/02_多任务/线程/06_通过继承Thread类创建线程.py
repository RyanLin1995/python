import threading
import time


class MyThread(threading.Thread):

    def run(self):

        self.test1()

        self.test2()

    def test1(self):

        for i in range(5):
            time.sleep(1)
            print("---test1-1---{}".format(i))

    def test2(self):

        for i in range(10):
            time.sleep(1)
            print("---test1-2---{}".format(i))


class MyThread2(threading.Thread):

    def run(self):

        self.test1()

        self.test2()

    def test1(self):

        for i in range(5):
            time.sleep(1)
            print("---test2-1---{}".format(i))

    def test2(self):

        for i in range(10):
            time.sleep(1)
            print("---test2-2---{}".format(i))


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread2()
    t1.start()
    t2.start()
