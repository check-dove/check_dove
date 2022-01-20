from socketserver import (TCPServer as tcp,
                          StreamRequestHandler as srh)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyTrquertHandler(srh):
    def handle(self):
        print('...connected from:', self.client_address)
        # 接收到一个来自客户端的消息时，它就会调用 handle()方法。而 StreamRequestHandler
        # 类将输入和输出套接字看作类似文件的对象，因此我们将使用 readline()来获取客户端消息，
        # 并利用 write()将字符串发送回客户端。
        self.wfile.write(bytes(
            '[%s] %s' % (
                ctime(), self.rfile.readline().decode()), 'utf-8'))
        # what happens if you don't decode it here?


tcpServ = tcp(ADDR, MyTrquertHandler)
print('waiting for connection...')
tcpServ.serve_forever()
