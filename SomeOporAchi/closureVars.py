#!/usr/bin/env python
from time import time

# output = '<int %r id=%#0x cal=%d>'
# w = x = y = z = 1
# 
# def f1():
#     x = y = z = 2
# 
#     def f2():
#         y = z = 3
# 
#     def f3():
#         z = 4
# print(output % ('w', id(w), w))
# print(output % ('x', id(x), x))
# print(output % ('y', id(y), y))
# print(output % ('z', id(z), z))
# 
# clo = f3.func_closure
# if clo:
#     print("f3 closure vars:", [str(c) for c in clo])
# else:
#     print("no f3 closure vars")
# f3()
# 
# clo = f2.func_closure
# if clo:
#     print("f2 closure vars:", [str(c) for c in clo])
# else:
#     print("no f2 closure vars")
# f2()
# 
# clo = f1.func_closure
# if clo:
#     print("f1 closure vars:", [str(c) for c in clo])
# else:
#     print("no f1 closure vars")
# f1()

"""--------------------------------------------------------------------------------"""
"""                                 含参数的装饰器                                    """
"""--------------------------------------------------------------------------------"""


# 含闭包的装饰器
def logged(when):
    def log(f, *args, **kargs):
        print("""Called:
        function: {} 
        args: {} 
        kargs: {}""".format(f, args, kargs))

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f,*args,**kargs)
                print("time delta:{}".format(time()-now))
        return wrapper

    try:
        return {'pre': pre_logged, 'post': post_logged}[when]
    except KeyError as e:
        raise ValueError(e)


@logged("pre")
def helo(name):
    print("hello,", name)


helo("world")
