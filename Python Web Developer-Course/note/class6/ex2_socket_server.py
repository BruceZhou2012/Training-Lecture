# coding:utf-8
__author__ = 'gubaoer'

import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen(5)  # 允许几个人等待，一般做法为5

while True:
    conn, addr = sk.accept()  # 等待接受请求,阻塞，没有请求就一直处于挂起
    print addr
    conn.sendall('welcome')  # 发送到一个缓冲区
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            conn.sendall('close')
            flag = False
        else:
            conn.sendall("sb")
    conn.close()
