"""
    背后的主要动机源自python面向对象编程。装饰器是在函数调用之上的修饰。
这些修饰仅在当声明一个函数或者方法的时候，才会额外调用。
    @decomaker(deco_args)
    def foo():pass
    decomaker()用deco_aegs做了些事并返回一个函数对象，而foo作为其返回对象的参数，简单来说就是：
        foo = decomaker(deco_args)(foo)


    什么是装饰器？
        答：装饰器实质上就是函数。他们接受函数对象。
    装饰器如何处理被装饰的函数？
        答：我们在执行函数之前，可以运行一些预备代码，如post-morrem分析，也可以在执行代码之后做
    一些清理工作。所以当你看见一个装饰器函数的时候，里面很可能有一些定义了某个函数并在定义内的某处嵌
    入了对目标函数的调用或者至少一些引用。故可以考虑在装饰器中置入通用功能的代码来降低程序的复杂度。

    装饰器能用来干什么？
        答：例如，可以用装饰器来：·引入日志·增加计时逻辑来检测性能·给函数加入事物的能力。
"""
"""
    闭包：将内部函数自己的代码和作用域以及外部函数的作用结合起来。 
闭包的词法变量不属于全局名字空间域或者局部的--而属于其他的名字空间，带着“流浪"的作用域。 
    
    
    
    
    
    注：closures 在函数式编程中是一个重要的概念，Scheme 和 Haskell 便是函数
式编程中两种。
        Closurs 对于安装计算， 隐藏状态， 以及在函数对象和作用域中随意地切换是很有用的。 closurs
在 GUI 或者在很多 API 支持回调函数的事件驱动编程中是很有些用处的。以绝对相同的方式，应用
于获取数据库行和处理数据。回调就是函数。闭包也是函数，但是他们能携带一些额外的作用域。
它们仅仅是带了额外特征的函数……另外的作用域。
"""

from time import ctime, sleep


def tsfunc(func):
    print('Thie is tsfunc')
    def wrappedFunc():
        print('[{}] {}() called'.format(ctime(), func.__name__))
        return func()
    return wrappedFunc


@tsfunc
def foo():
    print("This is PHiMiP")


def show_decorator_func():
    foo()
    sleep(4)

    for i in range(2):
        sleep(1)
        foo()


def convert(func, seq):
    ''' conv. sequence of numbers to same type '''
    return [func(eachNum) for eachNum in seq]


def show_convert():
    myseq = (123, 45.67, -6.2e8, 9999999999)
    print(convert(int, myseq))
    print(convert(float, myseq))


# 闭包
def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr


def show_closure():
    a = counter(5)
    for i in range(10):
        print(a())


if __name__ == '__main__':
    show_decorator_func()