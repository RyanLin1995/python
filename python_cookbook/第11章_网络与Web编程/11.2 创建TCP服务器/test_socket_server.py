import socket
from socketserver import StreamRequestHandler, TCPServer, BaseRequestHandler


# 基础应答服务器
# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('Got connection from', self.client_address)
#         while True:
#
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)

# 接收的信息需要有\n结尾
class EchoHandler(StreamRequestHandler):
    # Optional settings (defaults shown)
    timeout = 5  # Timeout on all socket operations
    rbufsize = -1  # Read buffer size
    wbufsize = 0  # Write buffer size
    disable_nagle_algorithm = False  # Sets TCP_NODELAY socket option

    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out!')


if __name__ == '__main__':
    server = TCPServer(('127.0.0.1', 15000), EchoHandler)
    server.serve_forever()
