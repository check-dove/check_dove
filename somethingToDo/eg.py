# from time import sleep
# from math import pi
# import operator as ac
# import sys
import time

# import datetime

"""第二章练习"""


def python_2_7():
    i = 0
    k = input('please input integer:')
    while i in range(len(k)):
        print(k[i])
        sleep(1)
        i += 1
    for i in range(len(k)):
        print(k[i])
        sleep(1)


def python_2_8(l=0, j=0):
    """
        2-10：对输入的内容进行判断
        数字：isdigit()

    :param l:
    :param j:
    :return:
    """
    k = []  # [2, 4, 66, 66, 2]
    su = 0
    # for i in range(5):
    #     k.append(int(input('please input the integer:')))

    '''对输入的符号用isdigit()函数进行纯数字判断，数字存储到list中'''
    while 1:
        j = input('please input the integer:')
        if j == 'end':
            break
        elif j.isdigit():
            k.append(int(j))
        else:
            print('input is not integer')
            continue

    '''对list中的值进行求和'''
    su = sum(k)
    # for a in k:
    #     sum += a
    print(su)


def python_2_9():
    avg_list = [14, 18, 32, 4, 2]
    # su = 0
    # for i in avg_list:
    #     sum += i
    avg = sum(avg_list) / len(avg_list)
    print(avg)
    sleep(5)


"""第三章的作业，已经写了，主要体现为text_开头的两个文件"""

"""第四章练习"""
"""
1、id、type、value
2、指的是数据值不能改变，赋值操作将失败。可更改类型：列表、字典、变量
3、按顺序访问：列表、字符串、元组，映射类型通过键来访问对应的值，无顺序存储的
4、type是检测对象的类型的，返回的对象是一个类型字符串
5、str生成一个可读性较好的字符串表示，适合输出；repr得到的字符串通常可以用来重新获取该对象；repr和‘’类似
6、==调用的对象的__eq__方法（值比较），is调用的是id方法进行的比较（身份比较）
7、
8、列表和元组相同点：都是顺序访问且通过下标访问、存储类型都为容器类型——即可以存储多个数据，不同：是否能够更新
9、
"""

"""第五章练习"""
"""
1、 普通整形在大多32位机器上，取值范围为-2**32~2**32-1
    长整型能表达的数值取决于机器支持（虚拟）的内存大小；
    长整型为普通整形的超集，在整形后面加L，表示为长整型；不过逐渐统一为一种。
2、
"""


def eg_5_3_pra(cord):
    """
        输入一个对象，判断其所在等级
    ：method    if-elif变相实现switch语句
    :param cord:数字
    :return: 等级：“A、B、C、D、E”
    """
    excellent = 'A'
    good = 'B'
    medium = 'C'
    pas = 'D'
    fail = 'E'
    if 90 < cord <= 100:
        return excellent
    elif 80 < cord <= 89:
        return good
    elif 70 < cord <= 79:
        return medium
    elif 60 < cord <= 69:
        return pas
    else:
        return fail


def eg_5_4_pra(thisyear=1990):
    """
    ：method 在这用了一个eval函数对表达式进行求值的操作，还有迭代器的next方法返回下一个内容
    :param thisyear: 传入当前年份，默认为1990
    :return: 返回当前年份开始算的下一个闰年
    """
    year = range(thisyear, 3000)
    condition = '(eachitem % 4 == 0 and eachitem % 100 != 0) ' \
                'or (eachitem % 4 == 0 and eachitem % 100 == 0)'
    runyear = iter([eachitem for eachitem in year if eval(condition)])
    return next(runyear)


def eg_5_5_pra(amount, money):
    """
        找零（几张十元、五十元等详细的金额）
    :Notice 用普通加减法有时候会少一点钱，还是二进制对小数的存储问题，
            对金钱的计算还是不要用这种方法了，要丢钱
    :param amount: 超市购物需支付amount
    :param money: 给了money
    :return: 找零（几张十元、五十元等详细的金额）数据结构
    """
    # 甚至我们还可以设置一个钱柜有的面值更新，将用找零用完了的面值，从系统中清除，倘若补齐了，就进行增加
    denomination = [0.1, 0.5, 1, 5, 10, 20, 50, 100]
    data = money - amount
    outputdict = {}.fromkeys(denomination)
    number = 0
    for eachitem in reversed(denomination):
        print('eachitem=', eachitem)
        while data - eachitem >= 0:
            data -= eachitem
            number += 1
            outputdict[eachitem] = number
            print('data=', data)
        number = 0
        if data == 0:
            break
    return outputdict


def eg_5_6_pra(exp):
    """
            实现一个eval函数(先放一放)
    :param exp:
    :return:
    """


def eg_5_10_pra(temp):
    return (temp - 32) * (5 / 9)


def eg_5_12_pra():
    dir(sys)
    print(sys.maxsize.__int__())
    print(sys.float_info)


def eg_5_13_pra():
    """
        写一个函数，把由小时和分钟表示的时间转换为只用分钟表示的时间
    :return:
    """
    thistime = time.time()
    structtime = time.localtime(thistime)
    curtimeofm = time.strftime('%M', structtime)
    curtimeofh = time.strftime('%H', structtime)
    return str(60 * int(curtimeofh) + int(curtimeofm)) + 'M'


def eg_5_14_pra(principal, **depositintandper):
    """
        银行利息：写一个函数，以定期存款利率为参数，假定该账户每日计算复利，
                请计算并返回年回报率
    :return:
    """
    # depositt = datetime.datetime.fromtimestamp(deposittime)
    # nextdepositt = datetime.datetime.now()
    # print(nextdepositt-depositt)
    # if nextdepositt-depositt>=1:
    #     depositt += 1
    for i in depositintandper.keys():
        pri = principal * float(i) * depositintandper[i]
        print(pri)


def show_eg_5_14_pra():
    deposit = {'0.0135': 1, '0.0155': 1, '0.0175': 1, '0.0225': 1, '0.0275': 1}
    eg_5_14_pra(10000, **deposit)


def eg_5_16_payment(balance, paid):
    """
        家庭财务显示
    :param balance:剩余金额
    :param paid:每月支出金额
    :return: 这里设置的元素为字符串的列表
    :描述 ：输出结果应该类似鞋面的格式（数字仅用于演示）
        Enter opening balance:100.00
        Enter monthly payment: 16.13
        Amount Remaining
        Pymt# Paid Balance
        ----- ------ ---------
        0 $ 0.00 $100.00
        1 $16.13 $ 83.87
        2 $16.13 $ 67.74
        3 $16.13 $ 51.61
        4 $16.13 $ 35.48
        5 $16.13 $ 19.35
        6 $16.13 $ 3.22
        7 $ 3.22 $ 0.00
    """
    currency = '$'
    prinlist = []
    for i in range(8):
        if i == 0:
            balance = balance
            pai = 0
        elif float(balance) - float(paid) > 0:
            balance = float(balance) - float(paid)
            balance = round(balance, 2)
            pai = paid
        else:
            pai = balance
            balance = 0
        prinlist.append((str(i).center(9, " ") +
                         currency + str(pai).ljust(9, " ") +
                         currency + str(balance).ljust(9, " ")))
    return prinlist


def show_rg_5_16_pyment():
    balance = input('Enter opening balance: ')
    paid = input('Enter monthly payment: ')
    print('Amount Remaining')
    printitem = 'Pymt'.center(9, " ") + 'Paid'.ljust(9, " ") + 'Balance'.ljust(9, " ")
    print(printitem)
    print('-' * len(printitem))
    backvalue = eg_5_16_payment(balance, paid)
    for i in backvalue:
        print(i)


def eg_5_17_pra():
    """
        生成一个有 N 个元素的由随机数 n 组成的列表， 其中 N 和 n 的取值范围分别为： (1 <
    N <= 100), (0 <= n <= 231 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数
    出来， 对它们排序，然后显示这个子集。
    :return:
    """
    import random
    N = random.randint(1, 100)
    temp = []  # list
    temp2 = [] # sublist
    for i in range(N):
        temp.append(random.randint(0, 230))
    for i in range(1, N):
        temp2.append(random.choice(temp))
    print(temp2)
    # return temp2


"""第六章练习"""

"""第七章练习"""

"""第八章练习"""

"""第九章练习"""

"""第十章练习"""

"""第十一章练习"""

"""第十二章练习"""

if __name__ == '__main__':
    pass
