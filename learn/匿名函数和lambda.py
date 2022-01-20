"""
        内建函数 apply()、filter()、map()、reduce()和lambda
        这些函数提供了在 python 中可以找到的函数式编程的特征。lambda 函数可以很好的和
    使用了这些函数的应用程序结合起来，因为它们都带了一个可执行的函数对象，lambda 表达式提
    供了迅速创造这些函数的机制。

            内建函数                                 描述
    apply(func[, nkw][, kw])    用可选的参数来调用 func，nkw 为非关键字参数，kw 关
                                键字参数；返回值是函数调用的返回值。
                                注：可以有效的取代 1.6，在其后的 python 版本中逐渐淘汰。

    filter(func, seq)           调用一个布尔函数 func 来迭代遍历每个 seq 中的元素； 返回一个
                                使 func 返回值为 ture 的元素的序列。

    map(func, seq1[,seq2...])   将函数 func 作用于给定序列（s)的每个元素，并用一个列表来提
                                供返回值；如果 func 为 None， func 表现为一个身份函数，返回
                                一个含有每个序列中元素集合的 n 个元组的列表。
                                注：由于在 python2.0 中，列表的综合使用的引入，部分被摈弃。

    reduce(func, seq[, init])   将二元函数作用于 seq 序列的元素，每次携带一对（先前的结果
                                以及下一个序列元素），连续的将现有的结果和下雨给值作用在获
                                得的随后的结果上，最后减少我们的序列为一个单一的返回值；如
                                果初始值 init 给定，第一个比较会是 init 和第一个序列元素而不
                                是序列的头两个元素。
"""

"""
    偏函数的应用（PFA）：
                简单的函数式例子：通过使用 functional 模块中的 partial（）函数来创建 PFA
                from operator import add, mul
                from functools import partial
                mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
                
    PFAs 也扩展到所有可调用的东西，如类和方法。“部分类实例化”。
                    
"""
import tkinter
from functools import partial


root = tkinter.Tk()
# partial统一部分参数，使之在风格上表现一致----部分实例化
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()