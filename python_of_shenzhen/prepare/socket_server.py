import socket
import subprocess


s = socket.socket()

host = '127.0.0.1'
port = 1888
s.bind((host, port))
s.listen(4)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        print(data)
        if data == 'exit':
            conn.sendall('done')
        else:
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = cmd.communicate()
            conn.sendall('I already accept to your message: {0}'.format(stdout))
conn.close()


