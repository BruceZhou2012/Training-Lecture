#coding:utf-8
import socket,time
#Client端  长连接


#example 1

Host = '192.168.1.111'      ####远程服务器地址
port = 50007   ####远程服务器端口

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,port))

while 1:
    s.sendall('Hello,world')
    data = s.recv(1024)
    time.sleep(2)
    print 'Received',repr(data)
s.close()


