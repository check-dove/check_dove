#!/usr/bin/env python

dashes = '\n' + '-' * 50  # dashed line
exec_dict = {

    'f': """ # for loop
 for %s in %s:
    print(%s)
""",

    's': """ # sequence while loop
 %s = 0
 %s = %s
 while %s < len(%s):
     print(%s[%s])
     %s = %s + 1
 """,

    'n': """ # counting while loop
 %s = %d
 while %s < %d:
     print(%s)
     %s = %s + %d
 """
}


def main():
    ltype = input('Loop type? (For/While) ').lstrip()[0:1].lower()
    dtype = input('Data type? (Number/Seq) ').lstrip()[0:1].lower()

    if dtype== 'n':
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(start, stop, step))

    else:
        seq = input('Enter sequence: ')
        var = input('Iterative variable name? ')

    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)

    elif ltype == 'w':
        if dtype == 's':
            svar = input('Enter sequence name? ')
            exec_str = exec_dict['s'] % \
                       (var, svar, seq, var, svar, svar, var, var, var)
        elif dtype == 'n':
            exec_str = exec_dict['n'] % \
                       (var, start, var, stop, var, var, var, step)
    print(dashes)
    print('Your custom-generated code:' + dashes)
    print(exec_str + dashes)
    print('Test execution of the code:' + dashes)
    exec(exec_str)
    print(dashes)


if __name__ == '__main__':
    main()

"""     逐行解释
Lines 1–25
在脚本的第一部分，我们设置了两个全局变量。第一个是由一行破折号（即是名字）组成的静
态字符串，第二个则是由用于生成循环的骨架代码组成的字典。for 循环的健值是'f'，用于迭代序
列的 while 循环的则是"s"，而记数 while 循环的是'n‘
Lines 27–30
这里我们提示用户输入他（她）想要的循环类型和数据类型
Lines 32–36
选定数字； 给出开始， 停止， 以及增量值。 在这个部分的代码中， 第一次引入了内建函数 input()。
我们将在 14.3.5 小节中看到，input()和 raw_input()相似，因为它提示用户给出字符串输入，但是
不同于 raw_input()，input()会把输入当成 python 表达式来求值，即使用户以字符串的形式输入，
也会返回一个 python 对象
Lines 38–39
选定序列；这里以字符串的形式输入一个序列
Line 41
给出用户想要使用的迭代循环变量的名字
Lines 43–44
生成添加自定义内容的 for 循环。
Lines 46–50
生成迭代序列的 while 循环。
Lines 52–54
生成计数的 while 循环
Lines 56–61
输出生成的源代码及其执行后的结果
Lines 63–64
当直接调用该模块的时候，执行 main()
"""
