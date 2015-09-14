#coding:utf-8
import SocketServer
import commands


class MyTCPHandler(SocketServer.BaseRequestHandler):
    # numbers = 0
    def handle(self):
        """
            self.request is the TCP socket connected to the client
            :return:
            """
        while True:  # if no while true?
            self.data = self.request.recv(1024).strip()
            # self.numbers += 1
            print "{} wrote:".format(self.client_address[0])
            assert isinstance(self.data, object)
            if not self.data:  ##检查客户端有没有数据发送
                print 'client %s is dead' % self.client_address[0]
                break
            user_input = self.data.split()
            if user_input[0] == 'get':
                with open(user_input[1],'rb') as f:
                    self.request.sendall(f.read())

                self.request.send('FileTransferDone')
                continue
            cmdb_status, result = commands.getstatusoutput(self.data)
            if len(result.strip()) != 0:
                 self.request.sendall(result)
            else:
                self.request.sendall('Done')


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()


