import socket
from xmldata import *


def showpage():
    hostip = '127.0.0.5'
    portid = 21567
    buffer = 10240
    ADDR = (hostip, portid)

    tcpsersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsersock.bind(ADDR)
    tcpsersock.listen(5)

    while True:
        print('waiting for connection...')
        tcpclsock, addr = tcpsersock.accept()
        print('...connected from :', addr)
        data = tostring(covert('text', dictcon))
        tcpclsock.send(data)

        tcpclsock.close()
        print('...the connection is closed!')
    tcpsersock.close()


if __name__ == '__main__':
    showpage()
