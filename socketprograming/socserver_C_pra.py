from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpsock = socket(AF_INET, SOCK_STREAM)
    tcpsock.connect(ADDR)
    data = input("---please enter>>>")
    if not data:
        break
    tcpsock.send(bytes(data+'\r\n', 'utf-8'))
    data = tcpsock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())
    kis = data.decode()
    print(data.strip())
    print(kis.strip())
    tcpsock.close()
print('esc')
