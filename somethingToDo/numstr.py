#!/usr/bin/env python
from filecmp import cmp
""" python核心编程-第2版：P539：13.13.4---13.6
    need to be reimplemented
"""


class NumStr(object):

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self): # define for str()
        return '[%d :: %r]' % self.__num, self.__string
    __repr__ = __str__

    def __add__(self, other): # define for s+o
        if isinstance(other, NumStr):
            return self.__class__(self.__num + \
            other.__num, self.__string + other.__string)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __mul__(self, num): # define for o*n
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __nonzero__(self): # False if both are
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):# normalize cmp()
        return cmp(cmpres, 0)

    def __cmp__(self, other): # define for cmp()
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
               self.__norm_cval(cmp(self.__string, other.__string))