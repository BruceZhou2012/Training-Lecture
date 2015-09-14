import socket
'''
socket_obj = socket.socket()
socket_obj.connect(('127.0.0.1',9999))
while True:
    data = raw_input("please input command:")
    if len(data) == 0:
        continue
    socket_obj.sendall(data)
    recv_data = socket_obj.recv(1024)   # defind 8912
    # print recv_data
    if recv_data == 'Done':
        print recv_data
        break
    else:
       print recv_data
socket_obj.close()
'''
import socket

socket_obj = socket.socket()
socket_obj.connect(('127.0.0.1',8888))
while True:
    data = raw_input("please input command:")
    if len(data) == 0:
        continue
    socket_obj.sendall(data)
    recv_data = socket_obj.recv(1024)   # defind 8912
    print recv_data
socket_obj.close()