#coding:utf-8
import socket,os,commands
#Server端,服务器长连接
'''
#example1
Host = ''
port = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,port))
s.listen(1)              ####接受一个连接

while 1:
    conn,addr = s.accept()      ##当每个接受每个请求的时候，都知道是哪个http客户端信息

    print 'Connected by',addr
    data = conn.recv(1024)    #1024Bit字节  === 1k的数据
    if not data:
        break
    print 'reserve IP:', addr
    conn.sendall(data)
conn.close()
'''
'''
#example2   长连接 并且一直接受client数据；但是另开一个http连接就无法进行服务器通信
Host = ''
port = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,port))
s.listen(1)              ####接受一个连接

while 1:
    conn,addr = s.accept()      ##当每个接受每个请求的时候，都知道是哪个http客户端信息

    print 'Connected by',addr

    while 1:
        data = conn.recv(1024)    #1024Bit字节  === 1k的数据
        if not data:
            break
        print 'reserve IP:', addr
        conn.sendall(data)
conn.close()
由于accept是接受一个新的http连接，假设没有子循环，客户端一直在对服务器进行发数据，而此时服务器已经通过第一个循环进入第一个accept，就一直卡着

'''

###  # 模拟ssh协议
Host = ''
port = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,port))
s.listen(1)              ####接受一个连接

while 1:
    conn,addr = s.accept()      ##当每个接受每个请求的时候，都知道是哪个http客户端信息

    print 'Connected by',addr

    while 1:
        data = conn.recv(1024)    #1024Bit字节  === 1k的数据
        if not data:
            break
        print 'reserve IP:', addr
        #os.system(data)
        #cmd_resut = os.popen(data).read()
        cmd_status,result = commands.getstatusoutput(data)
        if len(result.strip()) != 0:
            print cmd_status,result
            conn.sendall(result)
        else:
            conn.sendall("DONE")
conn.close()



