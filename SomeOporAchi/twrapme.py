from time import time, ctime, sleep


class TimedWrapme(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    # 单下划线/双下划线。可对外隐藏方法/属性
    # 返回的什么，需要确认
    def _gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError("argument of 'c', 'm', or 'a' req'd")
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self._gettimeval(t_type))

    def get(self):
        self.__atime = time()
        return self.__data

    # 用于修改__data数据值，并更新修改和访问时间
    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return 'self.__data'

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    # 用于授权类对原始数据类型的方法的访问
    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)


def showtimewrapme():
    timewrappedobj = TimedWrapme(932)
    print(timewrappedobj._gettimeval('c'))
    print(timewrappedobj.gettimestr('c'))
    print(timewrappedobj.gettimestr('m'))
    print(timewrappedobj.gettimestr('a'))
    sleep(10)
    print(timewrappedobj)
    print(timewrappedobj.gettimestr('c'))
    print(timewrappedobj.gettimestr('m'))
    print(timewrappedobj.gettimestr('a'))


if __name__ == '__main__':
    showtimewrapme()