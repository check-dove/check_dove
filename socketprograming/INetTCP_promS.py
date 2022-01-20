# import socket
from socket import *
from time import ctime

"""
    表 2-1 常见的套接字对象方法和属性
    名 称 描 述
    ----服务器套接字方法----
    s.bind()                    将地址（主机名、端口号对）绑定到套接字上
    s.listen()                  设置并启动 TCP 监听器
    s.accept()                  被动接受 TCP 客户端连接，一直等待直到连接到达（阻塞）
    
    ----客户端套接字方法----
    
    s.connect()                 主动发起 TCP 服务器连接
    s.connect_ex()              connect()的扩展版本，此时会以错误码的形式返回问题，
                                而不是抛出一个异常
    
    ----普通的套接字方法----
    
    s.recv()                    接收 TCP 消息
    s.recv_into()①              接收 TCP 消息到指定的缓冲区
    s.send()                    发送 TCP 消息
    s.sendall()                 完整地发送 TCP 消息
    s.recvfrom()                接收 UDP 消息
    s.recvfrom_into()①          接收 UDP 消息到指定的缓冲区
    s.sendto()                  发送 UDP 消息
    s.getpeername()             连接到套接字（ TCP）的远程地址
    s.getsockname()             当前套接字的地址
    s.getsockopt()              返回给定套接字选项的值
    s.setsockopt()              设置给定套接字选项的值
    s.shutdown()                关闭连接
    s.close()                   关闭套接字
    s.detach()②                 在未关闭文件描述符的情况下关闭套接字，返回文件描述符
    s.ioctl()③                  控制套接字的模式（仅支持 Windows）
    
    ----面向阻塞的套接字方法----
    
    s.setblocking()             设置套接字的阻塞或非阻塞模式
    s.settimeout()④             设置阻塞套接字操作的超时时间
    s.gettimeout()④             获取阻塞套接字操作的超时时间
    
    ----面向文件的套接字方法----
    
    s.fileno()                  套接字的文件描述符
    s.makefile()                创建与套接字关联的文件对象
    
    ----数据属性----
    
    s.family①                   套接字家族
    s.type①                     套接字类型
    s.proto①                    套接字协议
    
    ① Python 2.5 中新增。
    ② Python 3.2 中新增。
    ③ Python 2.6 中新增，仅仅支持 Windows 平台； POSIX 系统可以使用 functl 模块函数。
    ④ Python 2.3 中新增。
    
    核心提示：在不同的计算机上分别安装客户端和服务器来运行网络应用程序
"""

"""
除了现在熟悉的 socket.socket()函数之外， socket 模块还提供了更多用于网络应用开发的
属性。其中，表 2-2 列出了一些最受欢迎的属性。
表 2-2 socket 模块属性
属 性 名 称                                     描 述

----数据属性----

AF_UNIX、 AF_INET、 AF_INET6①、
AF_NETLINK②、 AF_TIPC③              Python 中支持的套接字地址家族                         
SO_STREAM、 SO_DGRAM                 套接字类型（TCP=流， UDP=数据报）
has_ipv6④                           指示是否支持 IPv6 的布尔标记

----异常----

error                                套接字相关错误
herror①                             主机和地址相关错误
gaierror①                           地址相关错误
timeout                              超时时间

----函数----

socket()                            以给定的地址家族、套接字类型和协议类型（可选）创建一个套接字对象
socketpair()⑤                       以给定的地址家族、套接字类型和协议类型（可选）创建一对套接字对象
create_connection()                 常规函数，它接收一个地址（主机名，端口号）对，返回套接字对象
fromfd()                            以一个打开的文件描述符创建一个套接字对象
ssl()                               通过套接字启动一个安全套接字层连接；不执行证书验证
getaddrinfo()①                      获取一个五元组序列形式的地址信息
getnameinfo()                       给定一个套接字地址，返回（主机名，端口号）二元组
getfqdn()⑥                          返回完整的域名
gethostname()                       返回当前主机名
gethostbyname()                     将一个主机名映射到它的 IP 地址62
gethostbyname_ex()                  gethostbyname()的扩展版本，它返回主机名、别名主机集合和 IP 地址列表
gethostbyaddr()                     将一个 IP 地址映射到 DNS 信息；返回与 gethostbyname_ex()相同的 3 元组
getprotobyname()                    将一个协议名（如‘tcp’）映射到一个数字
getservbyname()/getservbyport()     将一个服务名映射到一个端口号，或者反过来；
                                    对于任何一个函数来说，协议名都是可选的
ntohl()/ntohs()                     将来自网络的整数转换为主机字节顺序
htonl()/htons()                     将来自主机的整数转换为网络字节顺序
inet_aton()/inet_ntoa()             将 IP 地址八进制字符串转换成 32 位的包格式，或者反过来（仅用于 IPv4 地址）
inet_pton()/inet_ntop()             将 IP 地址字符串转换成打包的二进制格式，或者反过来（同时适用于 IPv4 和 IPv6 地址）
getdefaulttimeout()/
setdefaulttimeout()                以秒（浮点数）为单位返回默认套接字超时时间；
                                    以秒（浮点数）为单位设置默认套接字超时时间
                                    
① Python 2.2 中新增。
② Python 2.5 中新增。
③ Python 2.6 中新增。
④ Python 2.3 中新增。
⑤ Python 2.4 中新增。
⑥ Python 2.0 中新增。

要获取更多信息，请参阅 Python 参考库中的 socket 模块文档。
"""

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcpsock = socket(AF_INET, SOCK_STREAM)
# udpsock = socket(AF_INET, SOCK_DGRAM)

tcpsock.bind(ADDR)
tcpsock.listen(5)
try:
    while True:
        print('waiting for connection')
        tcpCliSock, addr = tcpsock.accept()
        print('...conected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send(bytes('[' + ctime() + ']', 'utf-8') + data)
        tcpCliSock.close()
except (EOFError, KeyboardInterrupt) as e:
    tcpsock.close()
    print(e)
