# 函数重载，使Time60支持加减法和增量加法，并且使Time60实现格式输出
class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        # 实现符号填充有三种方法：
        # 1：string.ljust(2, '0')[string.rjust(2, '0')]
        # 2：object.zfill(2)
        # 3：格式化输出：%02d
        return '%02d:%02d' % (self.hr, self.min)

    # 新的对象通过调用类来创建。唯一的不同点在于，在类中，你一般不直接
    # 调用类名， 而是使用 self 的__class__属性，即实例化 self 的那个类，并调用它。由于
    # self.__class__与 Time60 相同，所以调用 self.__class__()与调用 Time60()是一回事。
    def __add__(self, other):
        h = self.hr + other.hr
        m = self.min + other.min
        if m >= 60:
            m -= 60
            h += 1
        return self.__class__(h, m)

    def __sub__(self, other):
        h = self.hr - other.hr
        if self.min < other.min:
            h -= 1
            m = self.min + 60 - other.min
        else:
            m = self.min - other.min
        return self.__class__(h, m)

    # 重点是返回self（即实例本身）
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

    __repr__ = __str__
