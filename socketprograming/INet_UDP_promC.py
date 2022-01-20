from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpsock = socket(AF_INET, SOCK_DGRAM)
udpsock.connect(ADDR)
while True:
    data = input("---please enter>>>")
    if not data:
        break
    udpsock.send(bytes(data, 'utf-8'))
    # tempdata = udpsock.recv(BUFSIZ)
    data, ADDR = udpsock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data, ADDR)
