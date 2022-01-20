#!/usr/bin/env python

class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def writer(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    # 要支持for loop，得定义__iter__方法，next方法要使用的话，也得定义
    def __iter__(self):
        return self.file


if __name__ == '__main__':
    f = CapOpen('../learn/a.txt', 'r')
    for eachLine in f:
        print(eachLine,)
