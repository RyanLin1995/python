import socket
import re


def server_client(client_socket, request):
    request_lines = request.splitlines()
    print(request_lines)

    file = ''
    try:
        # 要匹配的项为 GET /index.html HTTP/1.1
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
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
        html_content = file.read()
        file.close()
        print("数据收到了")
        response_body = html_content

        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:{}\r\n'.format(len(response_body))
        print("准备发回数据")
        # 在 response header 中添加
        # Content-Length，同时去掉close函数，使链接变为长连接
        # 长连接:通过同一个套接字不断获取数据，直至到数据获取完成为止。
        # 那么服务器的 response header 需要设置 Content-Length，让客户端知道数据已经发送完成，主动断开 socket 链接
        # 与长链接对应的是短链接，即服务器发送完数据就主动断开，客户端再请求数据，就要再使用新的 socket

        response_header += '\r\n'
        response = response_header.encode('utf-8') + response_body
        client_socket.send(response)
        print("数据发回去了")


def main():
    """用来完成整体控制"""

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 8081))

    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    client_socket_list = list()
    while True:
        try:
            client_socket, client_addr = tcp_server_socket.accept()
            print(client_addr)
        except Exception as ret1:
            pass
        else:
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)
            print(client_socket_list)

            for clientSocket in client_socket_list:
                try:
                    recv = clientSocket.recv(1024).decode('utf-8')
                except Exception as ret2:
                    pass
                else:
                    if recv:
                        print("数据来了")
                        server_client(clientSocket, recv)
                    else:
                        clientSocket.close()
                        client_socket_list.remove(clientSocket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
