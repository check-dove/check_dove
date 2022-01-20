"""
            变长参数：元组、字典（字典中键为参数名，值为相应的参数值）。
        元组对应额外的 非关键字参数  ；
        字典对应额外的 关键字参数   。

        对于这类函数的调用：
                        newfoo(2, 4, *(6, 8), **{'foo': 10, 'bar': 12})
            另外：
                    aTuple = (6, 7, 8)
                    aDict = {'z': 9}
                    newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)
            也是可以的，注意，在含有字典参数的函数定义中，所有参数最后必须为字典参数；
        在调用中，最后一位参数也同样必须为字典/关键字参数。
"""


def func_it_test(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, diag)
    return result


def func_it_self():
    funcs = (int, float, str)
    vals = (123, 12.23, '1233', '12.34')

    for eachfuncs in funcs:
        for eachvals in vals:
            retval = func_it_test(eachfuncs, eachvals)
            if retval[0]:
                print('%s(%s) =' % (eachfuncs.__name__, eachvals), retval[1])
            else:
                print('{}({})=FAIL:{}'.format(eachfuncs.__name__, eachvals, retval[1]))


if __name__ == '__main__':
    func_it_self()