from time import sleep
"""
    根据选择进行求和 sum 或求平均 avg 的小程序
"""

def python_2_9():
    avg_list = [14, 18, 32, 4, 2]
    sum = 0
    for i in avg_list:
        sum += i
    avg = sum/len(avg_list)
    print(avg)


def python_2_8(l=0):
    k = [2, 4, 66, 66, 2]
    sum = 0
    while l in range(len(k)):
        sum += k[l]
        l += 1
    print(sum)


def python(scan=None, temp=1):
    if scan == 'X' or scan == 'x':
        temp -= 1
        print('the exe is end')
    if scan == 'avg':
        python_2_9()
    if scan == 'sum':
        python_2_8()
    return temp


if __name__ == '__main__':
    o = 1
    while 1:
        if o != 1:
            break
        k = scan = input("请输入需要执行的选项：\n"
                         "1、avg\n"
                         "2、sum\n"
                         "3、退出（输入或者X）\n"
                         "输入为：")
        if k == 'avg' or k == 'sum' or k == 'x' or k == "X":
            o = python(scan=k)
        else:
            print("提示：请重新输入指定选项")
            sleep(1)
            continue

