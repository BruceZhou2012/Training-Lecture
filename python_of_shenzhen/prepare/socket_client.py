import socket

s = socket.socket()

s.connect(('127.0.0.1', 1888))

while True:
    data = raw_input("please input message:")
    s.sendall(data)
    data = s.recv(1024)
    print(data)
    if data == 'done':
        break
s.close()
