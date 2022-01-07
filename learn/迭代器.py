from random import choice


class RandSeq(object):
    """randseq：随机迭代序列， 无穷迭代， 十三章内容"""
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    # 这里随机迭代， 不会越界，从而无穷, 有限无穷
    def next(self):
        return choice(self.data)


# 可控返回数目的迭代器（一次返回几个对象），
# 并且用safe标志控制StopIteration异常的打印：
# 标识符(safe)为真，返回所获取的任意条目，为假(False)，则在用户请求过多条目时，将会引发一个异常。
class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retal = []
        for eachItem in range(howmany):
            try:
                retal.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retal


def showanyiter():
    # python2中的例子，如今报错：TypeError: iter() returned non-iterator of type 'AnyIter'
    # a = AnyIter(range(10))
    # i = iter(a)
    # for j in range(1, 5):
    #     print(j, ':', i.next(j))
    # python3中，改为如下，原因：3中，类和类型统一后，AnyIter返回的本身就是一个名为AnyIter的迭代器，
    # 故再此调用iter()会出错
    a = AnyIter(range(10))
    for j in range(1, 5):
        print(j, ':', a.next(j))
    a.next(14)


class MyNumbers:
    """迭代器示例：第八章例子"""
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    # 这里下一项迭代， 有界， 有StopIteration
    def __next__(self):
        x = self.a
        self.a += 1
        return x


def show_mynumber():
    myclass = MyNumbers()
    # myiter = iter(myclass)
    for i in range(100):
        print(next(myclass), end=',')


if __name__ == '__main__':
    showanyiter()
