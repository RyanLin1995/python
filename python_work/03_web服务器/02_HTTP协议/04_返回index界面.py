import socket


def server_client(client_socket):
    """为这个客户端返回数据"""
    request = client_socket.recv(1024)
    print(request)

    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'

    file = open('./html/index.html', 'rb')
    html_content = file.read()

    client_socket.send(response.encode('utf-8'))
    client_socket.send(html_content)

    client_socket.close()


def main():
    """用来完成整体控制"""

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 8081))

    tcp_server_socket.listen(128)

    while True:
        client_socket, client_addr = tcp_server_socket.accept()

        server_client(client_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()