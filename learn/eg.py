from time import sleep


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


def python_2_8(l=0,j=0):
    """
        2-10：对输入的内容进行判断
        数字：isdigit()

    :param l:
    :param j:
    :return:
    """
    k = [] #[2, 4, 66, 66, 2]
    sum = 0
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
    while l in range(len(k)):
        sum += k[l]
        l += 1
    # for a in k:
    #     sum += a
    print(sum)



def python_2_9():
    avg_list = [14, 18, 32, 4, 2]
    sum = 0
    for i in avg_list:
        sum += i
    avg = sum/len(avg_list)
    print(avg)
    sleep(5)


def python_3_1():
    a=0

if __name__ == '__main__':
    python_2_8()