from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpsock = socket(AF_INET, SOCK_DGRAM)
udpsock.bind(ADDR)
while True:
    print('waiting for connection')
    # data = udpsock.recv(BUFSIZ)
    data, addr = udpsock.recvfrom(BUFSIZ)
    udpsock.sendto(bytes('[%s] %s' % (ctime(), data), 'utf-8'), addr)
    print('...received from and returned to:', addr)
