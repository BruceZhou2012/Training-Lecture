import SocketServer

class MysocketServer(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if data == 'exit':
                self.request.sendall('Done')
            else:
                print data
                self.request.sendall("you input command is '%s'" % data)
if __name__ == "__main__":
    #x = MysocketServer(SocketServer.ThreadingTCPServer,'127.0.0.1',8888)
    #x.setup()
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8888), MysocketServer)
    server.serve_forever()





