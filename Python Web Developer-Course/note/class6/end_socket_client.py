import socket


socket_obj = socket.socket()
socket_obj.connect(('127.0.0.1',8888))
while True:
    input_data = raw_input('please input:')
    socket_obj.sendall(input_data)
socket_obj.close()