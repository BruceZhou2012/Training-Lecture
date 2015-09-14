# coding:utf-8
__author__ = 'gubaoer'

import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.connect(ip_port)

while True:
    data = sk.recv(1024)  # 8192
    print data
    if data == 'close':
        break
    inp = raw_input('Input:')
    f = file(inp,'rb')
    data = f.read()
    f.close()
    sk.sendall(data)
sk.close()