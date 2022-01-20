# 描述符是如何运作的？

# 使用文件来存储属性，雏形版本 in the book

# 编写一个描述符类，有一个属性：saved——记录描述符访问的所有属性。
# 描述符创建后将注册且记录所有从用户处接收的属性名

# 获取描述符之前，确保用户给他们赋值后才能使用，上述条件成立，尝试打开pickle文件以读取其中所保存的之。
# 如果打开失败，将引发一个异常：原因可能有：文件不存在/已损坏/由于某种原因打不开/不能被pickle模块反串行化

# 将属性保存到文件中需要经过以下几个步骤：打开用于写入的pickle文件，将对象串行化到磁盘，注册属性名
# 使用户可以读取这些属性值，如果对象不能被pickle{待统一命名，将引发一个异常。

# !/usr/bin/env python

import os
import pickle


class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError("{} used before assignment".format(self.name))

        try:
            f = open(self.name, 'rb')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError, AttributeError, ImportError
                , IndexError) as e:
            raise AttributeError("could not read {}".format(self.name))

    def __set__(self, obj, val):
        f = open(self.name, 'wb')
        try:
            pickle.dump(val, f)
            FileDescr.saved.append(self.name)
        except (TypeError, pickle.PicklingError) as e:
            raise AttributeError("could not pickle {}".format(self.name))
        finally:
            f.close()

    def __delete__(self, instance):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError) as e:
            pass


class MyFileVarClass(object):
    foo = FileDescr('foo.txt')
    bar = FileDescr('bar')


# 类的实例在填充属性的时候，描述符类是如何运行的？
def test_FileDescr():
    fvc = MyFileVarClass()
    fvc.foo = '23'
    fvc.bar = 'jianshe'
    print(fvc.foo,fvc.bar)


# 你明白 properties 是如何把你写的函数(fget, fset 和 fdel)影射为描述符的__get__(),
# __set__(), 和__delete__()方法的吗？
#
# property(fget=None, fset=None, fdel=None, doc=None)
# 请注意 property()的一般用法是，将它写在一个类定义中，property()接受一些传进来的函数
# (其实是方法)作为参数。实际上，property()是在它所在的类被创建时被调用的，这些传进来的(作
# 为参数的)方法是非绑定的，所以这些方法其实就是函数！
class ProtectAndHideX(object):
    def __init__(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = ~x

    def get_x(self):
        return ~self.__x

    x = property(get_x)


class HideX_1_0(object):
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = ~x

    x = property(get_x, set_x)


class HideX_mod_2_0(object):
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        def fget(self):
            return ~self.__x

        def fset(self, x):
            assert isinstance(x, int), '"x" must be an integer!'
            self.__x = ~x

        return locals()

    # 为什么会这样写，什么意思，怎么工作
    @x.setter
    def x(self, value):
        self._x = value
