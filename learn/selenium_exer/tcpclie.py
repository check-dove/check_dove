import socket
from xml.etree import ElementTree as Et


hostip = '127.0.0.5'
portid = 21567
buffer = 10240
ADDR = (hostip, portid)

tcpcliserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpcliserv.connect(ADDR)
data = tcpcliserv.recv(buffer)
entercon = Et.fromstring(data)
print(entercon)
tcpcliserv.close()
