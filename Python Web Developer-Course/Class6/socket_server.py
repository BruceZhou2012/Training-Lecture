import socket

# socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_obj = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
socket_obj.bind((HOST,PORT))
socket_obj.listen(5)
while True:
    conn, addr = socket_obj.accept()
    while True:
        data = conn.recv(1024)
        if data == 'exit':
            conn.sendall('Done')
        else:
            print data
            conn.sendall("you input command is '%s'" % data)
socket_obj.close()
