# cording = utf-8
from time import ctime, sleep
import threading


def test1():
    for i in range(3):
        print("this is test1 at {}".format(ctime()))
        sleep(1)


def test2():
    for i in range(3):
        print("this is test2 at {}".format(ctime()))
        sleep(1)


threads = []
# 当实例化一个Thread对象后，可用的方法有：
# start(),开始线程的活动
# run()，用来表示线程的活动
# join([timeout=None]).等待所有的子线程结束或者出现超时错误
# join返回的值为None，必须在join后调用alive()函数老判断是否超时
# name，仅用于识别目的的字符串。无语义。多个线程可能被赋予相同的名称。
# getName()，获取name值。
# setName()，设置name值。
# ident，线程的“线程标识符”，如果线程尚未启动，则为空。即使线程退出，标识符也是可用的。
# is_alive(),判断线程是否存在
# daemon(),一个bool值，表示线程是否是守护线程，必须在调用start前设置
# 否则会引发错误，初始值继承自创建线程，主线程不是守护线程，因此在主线程中
# 创建的所有线程默认不是守护线程。
# daemon值为False，意味着主线程结束时会检测该子线程是否结束，若还在运行
# 则主线程会等待它完成后再退出，但若为True，在主线程退出的时候这些子线程也会同时退出。
# 当没有存活的非守护进程的时候，整个python程序退出。
# 另外，一个先成功可以多次使用join()函数。如果尝试使用join()函数连接当前线程，
# join()将引发一个运行错误，导致死锁。
t1 = threading.Thread(target=test1)
t1.setName("I am number 1")
threads.append(t1)
t2 = threading.Thread(target=test2)
t2.setName("I am number 2")
threads.append(t2)

if __name__ == "__main__":
    print("start {}".format(ctime()))
    # test1()
    # test2()
    for t in threads:
        print(t.getName())
        t.setDaemon(True)
        t.start()
        print("magname is {}".format(t.ident))
        print("zhuname is {}".format(threading.get_ident()))
    # 锁定主线程，直到所有子线程执行完毕
    # 若去掉，很可能主线程已经执行完毕，而子线程还未执行完，程序就已经退出了
    t.join()
    print("done {}".format(ctime()))
