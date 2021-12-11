# cording = utf-8
from time import ctime
import time
import threading


def test1():
    for i in range(3):
        print("this is test1 at {}".format(ctime()))
        time.sleep(1)


def test2():
    for i in range(3):
        print("this is test2 at {}".format(ctime()))
        time.sleep(1)

threads = []
t1 = threading.Thread(target=test1)
t1.setName("I am number 1")
threads.append(t1)
t2 = threading.Thread(target=test2)
t2.setName("I am number 2")
threads.append(t2)

if __name__ == "__main__":
    # test1()
    # test2()
    for t in threads:
        print(t.getName())
        t.setDaemon(True)
        t.start()
        print("magname is {}".format(t.ident))
        print("zhu mag is {}".format(threading.get_ident()))
    t.join()
    print("done {}".format(ctime()))
