import marshal
import pickle
import shelve
"""
    marshal、pickle转换并存储对象，（为保存和传输提供方便）该过程即数据的扁平化或数据的序列化、顺序化
    另外一些*db*模块(dbhash/bsddb,dbm,gdbm,dumbdbm等)以及它们的"管理器"(anydbm)只提供了Python字
符串的永久性储存. 而模块shelve则两种功能都具备.

    区别：marshal只能处理简单的python对象（数字，序列，映射，以及代码对象）
        pickle还可以处理递归对象，被不同地方多次引用的对象，以及用户定义的类和实例，其还有一个增强的版本
    叫cPickle，使用c实现了相关功能
    
    *db*模块：提供一个类似字典和文件的对象，可以完成字符串的永久性存储。
        使用传统的DBM格式写入数据。不知道用哪个的时候最好使用anydbm
    
    shelve模块：提供了python对象的序列化和存储转换，以及类似字典和文件的对象，可以完成python对象的永久性存储
        使用anydbm模块寻找合适的DBM模块,然后使用cPickle来完成对储存转换过程.允许对数据库文件进行
    并发的读访问, 但不允许共享读/写访问. 
"""

f = open('../learn/smtp_exer/a.txt', 'r+')
pickle.load(f)
f.close()
