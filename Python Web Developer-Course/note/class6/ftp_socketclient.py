#coding:utf-8
import socket
Host = '192.168.1.111'      ####远程服务器地址
port = 50007   ####远程服务器端口

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,port))

while 1:
    cmd = raw_input('your command:').strip()
    if len(cmd) == 0:
        continue
    s.sendall(cmd)
    if cmd.split()[0] == 'get':
        with open(cmd.split()[1],'wb') as f:
            while True:
                data = s.recv(1024)
                if data == "FileTransferDone":break
                if not s.recv(1024):break
                f.write(s.recv(1024))
        continue
    else:
        print


    #time.sleep(2)

s.close()