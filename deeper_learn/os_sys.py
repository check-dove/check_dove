import os
import sys
"""
    os和os.path两个模块提供了访问计算机文件系统的不同方法，os.path侧重于文件路径及文件名的处理
    os可以完成更多工作，我们可以通过它管理进程环境，甚至可以让python程序与另一个执行中的程序对话
"""


def file_w_with_linesep():
    f = open('../learn/smtp_exer/a.txt', 'a+')
    while 1:
        aline = input('enter a line("." to quit):>')
        if aline != ".":
            f.write('%s%s' % (aline, os.linesep))
        else:
            break
    f.close()


def file_w_with_seek_tell():
    f = open('../learn/smtp_exer/a.txt', 'a+')
    a = f.tell()
    print('a={}'.format(a))
    while 1:
        aline = input('enter a line end with "." :>')
        if aline != ".":
            f.write('%s%s' % (aline, os.linesep))
        else:
            break
        if '.' in aline:
            break
    b = f.tell()
    print('b={}'.format(b))
    print(f.fileno())
    print(f.flush())
    f.close()
    if f.closed:
        print('It has been closed')
    else:
        print("File is not closed")


def os_os_path_sys_test():
    print('you entered', len(sys.argv), 'arguments...')
    print('they were::', sys.argv, type(sys.argv))
    a = os.walk('../learn')
    for i in a:
        print(i)
    dirlist = os.listdir('../learn')
    print(dirlist)


if __name__ == '__main__':
    os_os_path_sys_test()