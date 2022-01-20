import sys

"""----------------------------example in the book---------------------------------"""
"""                                    作用域                                       """
"""--------------------------------------------------------------------------------"""

# j, k = 1, 2
#
#
# def proc1():
#     j, k = 3, 4
#     print('j=%d and k=%d' % (j, k))
#     k = 5
#
#     def proc2():
#         j = 6
#
#     j = 8
#     proc2()
#     print('j=%d and k=%d' % (j, k))
#
#
# proc1()
# print("j={} and k={}".format(j, k))
#
# k = 7
# proc1()
# print('j=%d and k=%d' % (j, k))

""" 递归 """


# 阶乘
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


"""--------------------------------------------------------------------------------"""
"""                                 生成器                                          """
"""--------------------------------------------------------------------------------"""

"""
    什么是 python 式的生成器？
    答：从句法上讲，生成器是一个带 yield 语句的函数。一个函数或者子程序只返回一次， 
    但一个生成器能暂停执行并返回一个中间的结果----那就是 yield 语句的功能， 返回
    一个值给调用者并暂停执行。当生成器的 next()方法被调用的时候，它会准确地从离开
    地方继续。
    
    生成器特性
    答：与迭代器相似，生成器以另外的方式来运作：当到达一个真正的返回或者函数结束没有
    更多的值返回（当调用 next())，一个 StopIteration 异常就会抛出。
    
    为什么不对这使用真正的迭代器呢？许多动机源自能够迭代穿越序列，而这需要函数威力而
    不是已经在某个序列中静态对象。
    
    最适合使用这些个强大的构建的地方在哪？
    答：使用生成器最好的地方就是当你正迭代穿越一个巨大的数据集合，而重复迭代这个数据集合是
    一个很麻烦的事，比如一个巨大的磁盘文件，或者一个复杂的数据库查询。对于每行的数据，你希
    望执行非元素的操作以及处理，但当正指向和迭代过它的时候，你“不想失去你的地盘“。
    你想要抓取一块数据，比如，将它返回给调用者来处理以及可能的对（另外一个）数据库的插
    入，接着你想要运行一次 next()来获得下一块的数据，等等。状态在挂起和再继续的过程中是保留
    了的，所以你会觉得很舒服有一个安全的处理数据的环境。
"""


def simplegen():
    a = 1
    yield a
    yield '2 --> punch!'


def show_simplegen():
    myg = simplegen()
    print(myg)
    for i in myg:
        print(i)


"""在接下来的例子中，我们将要创建一个带序列并从那个序列中返回一个随机元素的随机迭代器："""

# from random import randint


# def randGen(aList):
#     while len(aList) > 0:
#         yield aList.pop(randint(0, len(aList) - 1))
#
#
# def showranGen():
#     a = list(range(0, 52))
#     for item in randGen(a):
#         print(item)


"""
    加强的生成器特性：
    在 python2.5 中，一些加强特性加入到生成器中，所以除了 next()来获得下个生成的值，用户
    可以将值回送给生成器[send()]，在生成器中抛出异常，以及要求生成器退出[close()]
"""


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


# import sys


def showcounter():
    """jianshenmgxhxfhxdghxgh"""
    count = counter(5)
    for i in range(0, 50):
        print(count.__next__())
    print(count.send(9))
    print(count.__next__())
    print("globals:", globals().keys())
    print("locals:", locals().keys())
    # count.close()
    # count.__next__()
    print(sys.modules.keys())


"""--------------------------------------------------------------------------------"""
"""                OO--OOP:类和实例,OOD,属性和方法;继承和多重继承                        """
"""--------------------------------------------------------------------------------"""

"""     静态方法学习"""

"""     组合 和 派生 实现一些其他属性和方法来增强对原来的类对象。
        当类之间有显著的不同，并且(较小的类)是较大的类所需要的组件时，组合表现得很好，但当
你设计“相同的类但有一些不同的功能”时，派生就是一个更加合理的选择了。
        我们都不想到从头开始设计这些类，因为这样做会重复创建通用的 AddressBook
类时的操作。包含 AddressBook 类所有的特征和特性并加入需要的定制特性不是很好吗？这就是类
派生的动机和要求。
"""


class TempAddPhone(object):
    a = {2003: 'Jack'}
    b = 10

    def __init__(self, nm, ph):
        self.phone = ph
        self.name = nm
        print('This is __init__!')

    def update_phonenumber(self, newph):
        self.phone = newph
        print('update {}\'s phone to:{}'.format(self.name, self.phone))


class EmpAddrBookEntry(TempAddPhone):
    def __init__(self, nm, ph, ids, ema):
        TempAddPhone.__init__(self, nm, ph)  # 在运行时，属于调用非绑定方法
        self.empid = ids
        self.email = ema

    def update_email(self, newem):
        self.email = newem
        print('update {}\'s eamil to:{}'.format(self.name, self.email))


def show_tempaddphone_and_empaddrbookenter():
    print(TempAddPhone.a)
    TempAddPhone.a[2003] = 'kol'
    print(TempAddPhone.a)
    b = TempAddPhone('John Doe', '408-555-1212')
    b.a[2003] = 'jianche'
    print(b.a)
    c = TempAddPhone('Jack Dan', '304-982-4063')
    b.update_phonenumber('14780085127')
    c.update_phonenumber('16892374129')
    print(dir(b))
    print(dir(TempAddPhone), '\n', b.a)
    print(TempAddPhone.a)
    b = EmpAddrBookEntry('b', 17792793218, 6, '8973432@qq.com')
    b.update_email('jianshe@163.com')
    print(dir(TempAddPhone))
    print('--' * 20)
    print(dir(EmpAddrBookEntry))
    print('--' * 20)
    print(TempAddPhone.__dict__)
    print('--' * 20)
    print(TempAddPhone.__dictoffset__)
    print('--' * 20)
    print(TempAddPhone.__weakrefoffset__)
    print('--' * 20)
    print(TempAddPhone.__init_subclass__())


class TStaticMethod:
    @staticmethod
    def foo():
        print('calling static method foo()'.ljust(40), 'jianshe')


class TClassMethod:
    @staticmethod
    def foo(self):
        print('calling class method foo()')
        print('foo() is part of class:', self.__class__)


# 特殊函数的重载（定制特殊函数） (简单的)
class RoundFloatManual(object):
    def __init__(self, val):
        try:
            assert isinstance(val, float), ''
            self.value = round(val, 2)
        except AssertionError as ae:
            print("Value must be a float!\n", "{}".format(ae))

    # 与显示有关的两个特殊函数
    def __str__(self):
        return '%.2f' % self.value

    def foo(self):
        pass

    def bar(self):
        pass

    # __repr__ = __str__


# 特殊函数的重载 （稍微复杂一点点的）  数值定制（Time60）
# from SomeOporAchi import Time60
# 多类型类定制：
# from somethingToDo import numst

# ###################################  私有化  ###################################### #
"""默认情况下，属性在 Python 中都是“public”，类所在模块和导入了类所在模块的其他模块的
代码都可以访问到。很多 OO 语言给数据加上一些可见性，只提供访问函数来访问其值。这就是熟知
的实现隐藏，是对象封装中的一个关键部分。
大多数 OO 语言提供“访问控制符”来限定成员函数的访问。
双下划线(__):
            由双下划线开始的属性在运行时被“混淆”，所以直接访问是不允许的。实际上，会在名字前面加上下
        划线和类名。比如，以例13.6(numstr.py)中的 self.__num 属性为例，被“混淆”后，用于访问这个
        数据值的标识就变成了self._NumStr__num。把类名加上后形成的新的“混淆”结果将可以防止在祖先类
        或子孙类中的同名冲突.(这种名字混淆的另一个目的,是为了保护__XXX 变量不与父类名字空间相冲突.)
单下划线(_):
          简单的模块级私有化只需要在属性名前使用一个单下划线字符。这就防止模块的属性用“ from mymodule
        import *”来加载。这是严格基于作用域的，所以这同样适合于函数。  
"""

# ###################################  包装  ####################################### #
"""意思是对一个已存在的对象进行包装，不管它是数据类型，还是一段代码，可以是对一个已存在的对象，增加
新的，删除不要的，或者修改其它已存在的功能。----------派生----继承
"""
# ###################################  授权  ####################################### #
"""授权是包装的一个特性，可用于简化处理有关 dictating 功能，采用已存在的功能以达到最大
限度的代码重用。
    实现授权的关键点就是覆盖__getattr__()方法，在代码中包含一个对 getattr()内建函数的调
用。特别地，调用 getattr()以得到默认对象属性（数据属性或者方法）并返回它以便访问或调用。
特殊方法__getattr__()的工作方式是， 当搜索一个属性时， 任何局部对象首先被找到（定制的对象）。
如果搜索失败了，则__getattr__()会被调用，然后调用 getattr()得到一个对象的默认行为。
    换言之，当引用一个属性时，Python 解释器将试着在局部名称空间中查找那个名字，比如一个
自定义的方法或局部实例属性。如果没有在局部字典中找到，则搜索类名称空间，以防一个类属性
被访问。最后，如果两类搜索都失败了，搜索则对原对象开始授权请求，此时，__getattr__()会被
调用。
"""

"""--------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------"""

if __name__ == "__main__":
    print(dir(RoundFloatManual))
    print(dir())
    print(dir(TStaticMethod))
    print(dir(counter()))
    print(dir(factorial))


