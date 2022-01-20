import os
from multiprocessing import Process
import time
"""
Table 14.6 执行外部程序的 os 模块函数
            (u 只对 unix 有效， w 只对 windows 有效）
os 模块函数                                         描述
system(cmd)                      执行程序 cmd（字符串），等待程序结束，返回退出代码（windows 下，始终为 0）
fork()                           创建一个和父进程并行的子进程[通常来说和 exec*()一起使用]； 返回两次....一次给父进程一次给子进程
execl(file, arg0,arg1,...)       用参数列表 arg0, arg1 等等执行文件
execv(file, arglist)             除了使用参数向量列表，其他的和 execl()相同
execle(file, arg0,arg1,... env)  和 execl 相同，但提供了环境变量字典 env
execve(file,arglist, env)        除了带有参数向量列表，其他的和 execle()相同
execlp(cmd, arg0,arg1,...)       于 execl()相同，但是在用户的搜索路径下搜索完全的文件路径名
execvp(cmd, arglist)             除了带有参数向量列表，与 execlp()相同
execlpe(cmd, arg0, arg1,... env) 和 execlp 相同，但提供了环境变量字典 env
execvpe(cmd,arglist, env)        和 execvp 相同，但提供了环境变量字典 env
spawn*a(mode, file, args[, env]) spawn*()家族在一个新的进程中执行路径，args 作为参数，也许还有环境变量的字典 env;模式（mode）是个显示不同操作模式的魔术。
wait()                           等待子进程完成[通常和 fock 和 exec*()一起使用] ○U
waitpid(pid,options)             等待指定的子进程完成[通常和 fock 和 exec*()一起使用] ○U
popen(cmd, mode='r',buffering=-1)执行字符串 cmd，返回一个类文件对象作为运行程序通信句柄，默认为读取模式和默认系统缓冲
startfileb(path)                 用关联的应用程序执行路径 W

"""
def temp_1_test():
    # os.system('dir')
    f = os.popen('dir .')
    file = open('../learn/mylog.txt', 'w+')
    for eachline in f.readlines():
        print(type(eachline))
        file.write(eachline)
    f.close()
    file.close()


"""
os.fork(), os.exec*(),os.wait*()

调用fork()的原始进程称为父进程，而作为该调用结果新创建的进程则称为子进程。当子进程返回的时
候， 其返回值永远是 0； 当父进程返回时， 其返回值永远是子进程的进程标识符（又称进程 ID,或 PID)
（这样父进程就可以监控所有的子进程了）PID 也是唯一可以区分他们的方式！

ret = os.fork()# spawn 2 processes, both return #产生两个进程，都返回
if ret == 0: # child returns with PID of 0 #子进程返回的 PID 是 0
    child_suite # child code #子进程的代码
else: # parent returns with child's PID #父进程返回是子进程的 PID
    parent_suite # parent code #父进程的代码
    
os.spawn*()
"""


def temp_2_test():
    ret = os.fork()
    if ret == 0:
        print('子进程', os.getpid())
    else:
        print('子进程', os.getpid())


class MynewProcess(Process):
    def run(self):
        while True:
            print("_____1_____")
            time.sleep(4)


if __name__ == '__main__':
    p = MynewProcess()
    p.start()
    while True:
        print("_____main_____")
        time.sleep(4)
