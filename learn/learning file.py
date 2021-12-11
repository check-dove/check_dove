import sys
from unicodedata import decimal
import openpyxl
import data


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
    if b==0:
        i += 1
    l = "iajsdjkshajhjasd"
    return i,l


def qwe():
    _, c = kil(b=0)
    a = 0
    for i, ch in enumerate(c):
        print(i, 'and', ch,)
    for i in range(int(len(c)-3)):
        if c[i:i+3]=='jhj':
            a = 1
            first = [list(c[:i]), c[i:i+3], list(c[i+3:])]
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
    """对三个数进行排序"""
    a = 0
    print("please input three digit:\n")
    l = int(input("1:\n"))
    j = int(input("2\n"))
    k = int(input("3\n"))
    if j > k:
        if l > j:
            # a = j
            # j = k
            # k = a
            j, k = k, j
            l, j = j, l
            # a = l
            # l = j
            # j = a
        elif k > l:
            pass
        else: l, k =k, l
            # a = l
            # l = k
            # k = a
    elif j > l:
        j, k = k, j
        # a = j
        # j = k
        # k = a
    elif l > k:
        l, j = j, l
        # a = j
        # j = l
        # l = a
    else:
        j, k = k, j
        k, l = l, k
        # a = j
        # j = k
        # k = l
        # l = a

    print("从小到大：{}<{}<{}".format(l, k, j))


def tes_1():
    all = []
    while 1:
        entry = input('>')
        if entry == '.':
            break
        else:
            all.append(entry)
    print(all)
if __name__ == '__main__':
    tes_1()