#coding:utf-8
import socket,time,commands
#Client端  长连接


#example 1
'''
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
'''
'''
Host = '192.168.1.111'      ####远程服务器地址
port = 50007   ####远程服务器端口

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,port))

while 1:
    cmd = raw_input('your command:').strip()
    s.sendall(cmd)
    data = s.recv(1024)
    #time.sleep(2)
    print data
s.close()
'''

##修复客户端直接输入回车的问题
Host = '192.168.1.111'      ####远程服务器地址
port = 50007   ####远程服务器端口

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,port))

while 1:
    cmd = raw_input('your command:').strip()
    if len(cmd) == 0:
        continue
    s.sendall(cmd)
    data = s.recv(1024)
    #time.sleep(2)
    print data
s.close()



