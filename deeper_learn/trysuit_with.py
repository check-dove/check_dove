"""
    try-except 和 try-finally 的一种特定的配合用法是保证共享的资源的
唯一分配,并在任务结束的时候释放它.比如文件(数据,日志,数据库等等),线程资源,简单同步,数
据库连接,等等. with 语句的目标就是应用在这种场景.
    然而，with 语句的目的在于从流程图中把 try,except 和 finally 关键字和资源分配释放相关
代码统统去掉, 而不是像 try-except-finally 那样仅仅简化代码使之易用.
    with context_expr [as var]:
        with_suite
    with语句仅能工作于支持上下文管理协议(context management protocol)的对象：(第一批成员)：
        . file
        . decimal.Context
        . thread.LockType
        . threading.Lock
        . threading.RLock
        . threading.Condition
        . threading.Semaphore
        . threading.BoundedSemaphore
"""