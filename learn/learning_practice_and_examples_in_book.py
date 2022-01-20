import sys
import urllib
import types
import os
from fontTools import unicodedata
from urllib3 import connection_from_url
import openpyxl
import re


def file_test():
    # f=open('a.txt','w')
    #
    # old=sys.stdout

    # logfile = open('casedata.xlsx')
    with openpyxl.Workbook('casedata.xlsx') as logfile:
        b = (dir(logfile), logfile.views, logfile.worksheets,
             logfile.sheetnames, logfile.excel_base_date, logfile.data_only)
    print(b)
    # print("hell world", file=logfile)
    logfile.close()


def kil(b=None):
    i = 1
    if b == 0:
        i += 1
    l = "iajsdjkshajhjasd"
    return i, l


def qwe():
    _, c = kil(b=0)
    a = 0
    for i, ch in enumerate(c):
        print(i, 'and', ch, )
    for i in range(int(len(c) - 3)):
        if c[i:i + 3] == 'jhj':
            a = 1
            first = [list(c[:i]), c[i:i + 3], list(c[i + 3:])]
            bq = first[1]
    if a == 1:
        print('{} is exist'.format(bq))
    else:
        print('{} is not exist'.format(bq))


class One_liushuai(object):
    def __init__(self, nm="iajsdjkshajhjasd"):
        self.c = nm

    def test_te_kil(self):
        sqdEvens = [(i, ch * 2) for i, ch in enumerate(self.c) if not i % 2]
        for k in sqdEvens:
            print(k)


def digit_sort():
    """ sort by three numbers """
    a = 0
    all = [None]*4
    print("please enter three numbers after '1,2,3',\n"
          "and enter 'end' to exit or any other start  to compare numbers after '4':\n")
    while 1:
        while 1:
            if a == 4:
                a = 0
                all[a-1] = None
            all[a] = input('{}:'.format(a+1))
            a += 1
            if all[3] is not None:
                break
        l = int(all[0])
        j = int(all[1])
        k = int(all[2])
        if l > j > k:
            j, k = k, j
            l, j = j, l
        elif j > k > l:
            pass
        elif j > l > k:
            l, k = k, l
        elif k > j > l:
            j, k = k, j
        elif l > k > j:
            l, j = j, l
        elif k > l > j:
            j, k = k, j
            k, l = l, k
        print("from min to max ：{}<{}<{}".format(l, k, j))

        if all[3] == 'end':
            break


def display_Num():
    """replenish of digit_sort"""
    all = []
    while 1:
        i = 0
        print("len:", len(all))
        if len(all) == 4:
            all.clear()
            i = 0
        jump = input("{}:".format(i))
        all.append(jump)
        i += 1
        if jump == 'end':
            break


def tes_1():
    # 手动输入数据为列表类型，并进行打印
    all = []
    while 1:
        entry = input('>')
        if entry == '.':
            break
        else:
            all.append(entry)
    print(all)

def tes_p():
    a = 'jianshemima'
    b = [None] + list(a.upper())
    if a.find('ans'):
        c = list(a[:a.index('ans')])
        c.append(a[a.index('ans'):a.index('ans')+len('ans')])
        c += list(a[a.index('ans') + len('ans'):])
        print(c)
    if 'ans' in c:
        print('in')
    v = str(c)
    print(v,type(v),';',b,'\n', ' '.join((a, 'join')))


def tes_pr():
    f = connection_from_url('http://'  # protocol
    'localhost'  # hostname
    ':8000'  # port
    '/cgi-bin/friends2.py')
    f.close()
    print(f)

def tes_pra():
    m = re.search(r'\\[rtfvn]', r'Hello World!\n')
    print(m)
    if m is not None:
        print(m.group())

def tes_practice():
    a = [1, 2, 3, 4]
    b = ['good', 'nice', 'bad', 'most']
    for i, j in zip(a, b):
        if j == 'nice':
            print(i, j)
    c = 't'
    print(unicodedata)


def one_jar():
    a = u'jianshemima oooshem ppshe\000\m lllllllllshem '
    c = a.replace(' ', ':', a.count(' ')-1)
    e = ':'.join(a.split())
    d = a.count(' ')
    # c = a.rfind('shem')
    print(d,c,type(c), '\n', e)


def alike():
    """Notice: use fromkeys to create a dictionary from a list"""

    a = ['jack', 'keko', 'job', 'kesy', 'nansy', 'job', 'jarbo']
    # for i in range(a.count('job')):
    #     a.remove('job')

    # remove duplicate elements from a list
    [a.remove('job') for i in range(a.count('job'))]
    # b = list(set(a))
    # b.sort(key=a.index)
    b = {}.fromkeys(a).keys()
    c = hash(tuple(a))
    print(b, c)


def just():
    a = ['jianshemia', 'wode', '1234']
    try:
        b = a.index('key')
    except ValueError as e:
        print('\'key\' is not in list')
    else:
        print(b)


def dict_tes():
    dict1 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
    c = dict1.setdefault('m', 'jianshe')
    print(c)
    print(dict1)


def set_test():
    a = ['jack', 'keko', 'job', 'kesy', 'nansy', 'job', 'jarbo']
    l = ['job', 'fox', 'girl', 'boy']
    b = set(a)
    print()


def while_for_test():
    """The password is valid for three times
    Example in book """
    passwdList = ['jianshemima', 'woshiyingxiong', '123456789wodemima']
    valid = False
    count = 1
    while count < 4:
        temp = input("enter password:> ")
        # check for valid passwd
        for eachPasswd in passwdList:
            if temp == eachPasswd:
                valid = True
                print("Hello, welcome back!")
                break
        if not valid:  # (or valid == 0)
            print("invalid input,and {} chances left.".format(3-count))
            if 3-count == 0:
                print("please try again tomorrow!")
            count += 1
            continue
        else:
            break


def list_comprehension():
    """=== 矩阵样例 ===
    你需要迭代一个有三行五列的矩阵么? 很简单:"""
    var = [(x + 1, y + 1) for x in range(3) for y in range(5)]
    print(var)

    """=== 磁盘文件样例 ===
    假设我们有如下这样一个数据文件
    hh.txt, 需要计算出所有非空白字符的数目:
    if we have a data file like 'hh.txt', 
    need to calculate the number of all non-blank characters
    """
    # calculate the number of words
    f = open('hh.txt', 'r')
    var1 = len([word for line in f for word in line.split()])
    print(var1)
    # calculate file size quickly
    var2 = os.stat('hh.txt').st_size
    print(var2)
    # calculate the number of all non-blank characters
    f.seek(0)
    # a = sum([len(word) for line in f for word in line.split()])
    # print(a)
    # compare two expr above and below
    b = sum(len(word) for line in f for word in line.split())
    print(b)


def file_test2():
    # truncate方法如何使用
    fo = open('smtp_exer/a.txt', 'r')
    fo.truncate(10)
    for eachline in fo:
        print(eachline, )
    fo.close()


def inner_function():
    print('This is inner function')

    def name_book():
        print('This is Jack')

    name_book()


def function_prac():
    inner_function()


def decorator_practice():
    print("this is a test!")


def foo():
    """ 嵌套作用语规则 """
    m = 3

    def bar():
        n = 4
        print(m + n)
        # 可调用外部函数的变量
        print(m)
    bar()


def mechanism_of_forloop():
    # for 循环机制
    seq = (123, 'xyz', 45.67)
    for i in seq:
        pass

    """The 'for' loop above works like this"""
    fetch = iter(seq)
    while True:
        try:
            fetch.__next__()
        except StopIteration:
            break
            pass


if __name__ == '__main__':
    """test of practice"""
    foo()



