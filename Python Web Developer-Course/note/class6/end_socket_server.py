import socket

socket_obj = socket.socket()
host = '127.0.0.1'
port = 8888
socket_obj.bind((host,port))
socket_obj.listen(4)
while True:
    conn,address = socket_obj.accept()
    while True:
        data = conn.recv(1024)
        print data
socket_obj.close()

