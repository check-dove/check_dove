"""
                    以下代码是书中的代码（为python2在unix上执行的），修改后在windows上执行
"""
import os
import socket
import errno
import tempfile


"""     定义了我们的新异常.      """


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    """
            "更新"异常的参数.原来的异常提供给我们一个参数集,希望获取这些参数并让其成为我们新的异常的一部分,
    嵌入或添加第三个参数.
    :param args:
    :param newarg:
    :return:
    """
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)
    return tuple(myargs)


def fileArgs(file, mode, args):
    """
            寻找表示"permissiondenied.(没有权限.)"的错误 EACCES.其他所有的 IOError 异常我们将不加修改
            最后我们把文件名加入参数列表,并以元组形式返回参数.
    :param file:
    :param mode:
    :param args:
    :return:
    """
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)
        myargs.append(args.filename)
    else:
        myargs = args
    return tuple(myargs)


def myconnect(sock, host, port):
    """
            conect()当网络连接失败时提供一个 IOError 类型的异常.
    socket.error 异常没有直接提供的错误号,我们为了遵循 IOError 协议,
    提供了一个错误号-错误字符串对,我们查找最接近的错误号.我们选用的 ENXIO.
    :param sock:
    :param host:
    :param port:
    :return:
    """
    try:
        sock.connect((host, port))
    except socket.error as args:
        myargs = updArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])
        raise NetworkError(updArgs(myargs, host + ':' + str(port)))


def myopen(file, mode='r'):
    """
            仅仅捕捉 IOError 异常.
    所有的其他都忽略并传给下一层(仅仅捕捉 IOError 异常.所有的其他都忽略并传给下一层
            一旦捕捉到 IOError 我们引发我们自己的异常并通过 fileArgs()返回值来定制参数.
    :param file:
    :param mode:
    :return:
    """
    try:
        fo = open(file, mode)
    except IOError as args:
        raise FileError(fileArgs(file, mode, args))
    return fo


def filetest():
    """
            可以手工的修改其权限来造成权限错误
            用 4 种不同的权限配置.零标示没有任何权限,0100 表示仅能执行,0400 表示只
读,0500 表示只可读或执行(0400+0100).
            用一种无效的方式打开文件
            如果发生错误,我们希望可以显示诊断的信息
            如果文件被打开成功,也就是权限由于某种原因被忽略.我们通过诊断信息指明并关闭文件.当
所有的测试都完成时,我们对文件开启所有的权限然后用 os.unlink()移除(os.remove()等价于
os.unlink()).
    :return:
    """
    path_file_temp = tempfile.mktemp(dir='/learn')
    path_file = os.path.split(path_file_temp)
    file = path_file[1]
    print('file name is :', file)
    f = open(file, 'w+')
    f.close()
    if os.path.exists(path_file_temp):
        print('{} exists'.format(file))

    for eachTest in ((0, 'r'), (0o664, 'r'),
                     (0o661, 'w'), (0o662, 'w')):
        try:
            os.chmod(path_file_temp, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError as args:
            print("{}: {}".format(args.__class__.__name__, args))
        except FileNotFoundError as args:
            print('file not found')
        else:
            print(file, "opened ok...perm ignored.")
        f.close()

        os.chmod(path_file_temp, 0o777)
        os.unlink(path_file_temp)


def nettest():
    """
            测试了我们的网络异常.套接字是一个用来与其他主机建立连接的通信
端点.我们创建一个套接字,然后用它连接一个没有接受我们连接的服务器的主机和一个不存在于我
们网络的主机
    :return:
    """
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, eachHost, 8080)
        except NetworkError as args:
            print("{}: {}".format(args.__class__.__name__, args))


if __name__ == '__main__':
    nettest()
