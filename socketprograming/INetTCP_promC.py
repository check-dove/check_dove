from socket import *
from time import ctime



HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpsock = socket(AF_INET, SOCK_STREAM)
tcpsock.connect(ADDR)
while True:
    data = input("---please enter>>>")
    if not data:
        break
    tcpsock.send(bytes(data, 'utf-8'))
    data = tcpsock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpsock.close()
