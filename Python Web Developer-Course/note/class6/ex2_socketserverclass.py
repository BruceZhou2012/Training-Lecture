__author__ = 'gubaoer'

import SocketServer


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        # print self.request
        # print self.client_address
        while True:
            # conn, addr = self.request.accept()
            conn = self.request
            conn.sendall('welcome')
            flag = True
            while flag:
                data = conn.recv(1024)
                print data
                if data == 'exit':
                    conn.sendall('close')
                    flag = False
                else:
                    conn.sendall("sb")
            conn.close()


ip_port = ('127.0.0.1', 9999)
sock = SocketServer.ThreadingTCPServer(ip_port, MyServer)
sock.serve_forever()
