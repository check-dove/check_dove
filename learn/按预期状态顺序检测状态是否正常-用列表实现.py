def test_pro1():
    lists = strs = sets = temp = []
    excep = ['list', 'set', 'str']
    objec = ['list', 'list', 'list', 'set', 'set', 'str', 'str', 'str', 'str', 'str', 'list']
    for i, element in enumerate(objec):
        if element == 'list':
            lists.append(i)
        if element == 'set':
            sets.append(i)
        if element == 'str':
            strs.append(i)
    for attrs in (lists, sets, strs):
        [print(f'存在错误状态{objec[attrs[i+1]]},为第{attrs[i+1]}个状态值') for i in range(len(attrs) - 1) if attrs[i + 1] - attrs[i] != 1]
    for i in excep:
        temp.append(objec.index(i))
    temp.sort()
    for i in range(len(excep)):
        if objec[temp[i]] != excep[i]:
            print("第%s状态错误" % (i+1))


if __name__ == '__main__':
    test_pro1()
