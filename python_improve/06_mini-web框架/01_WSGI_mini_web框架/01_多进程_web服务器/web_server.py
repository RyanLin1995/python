import socket
import re
import multiprocessing


class WSGIServer(object):

    def __init__(self):

        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(('', 8081))

        self.tcp_server_socket.listen(128)

    def server_client(self, client_socket):
        """为这个客户端返回数据"""
        request = client_socket.recv(1024).decode('utf-8')
        request_lines = request.splitlines()
        print(request_lines)

        try:
            # 要匹配的项为 GET /index.html HTTP/1.1
            ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])  # [^/]+ 表示匹配不是 / 的所有内容
            if ret:
                file_name = ret.group(1)
                if file_name == '/':
                    file_name = '/index.html'
                file = open('./html{}'.format(file_name), 'rb')
        except:
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            response += '\r\n'
            response += '-----Page not found -----'
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
        else:
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            html_content = file.read()
            file.close()
            client_socket.send(response.encode('utf-8'))
            client_socket.send(html_content)

        client_socket.close()

    def run_forever(self):
        """用来完成整体控制"""

        while True:
            client_socket, client_addr = self.tcp_server_socket.accept()

            p1 = multiprocessing.Process(target=self.server_client, args=(client_socket,))
            p1.start()

            client_socket.close()

        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web服务器对象，调用run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()