import socket


def server_client(client_socket):
    """为这个客户端返回数据"""
    request = client_socket.recv(1024)
    print(request)

    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    response += '<h1>hahahahaha</h1>'
    client_socket.send(response.encode('utf-8'))

    client_socket.close()


def main():
    """用来完成整体控制"""

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 因为 tcp 三次握手和四次挥手中，谁调用了 close，谁就需要等待2-5分钟，确保最后的 ack 发送成功。 如果是服务器先调用
    # close，且服务器是使用固定端口的。那么将会有2-3分钟内端口无法使用。 因此加上
    # tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
    # 1) 可以使地址和端口重复利用而不用等待。但是会有安全风险。因为某些操作系统允许不同地址绑定统一端口。例如0.0.0.0:80 和
    # 127.0.0.1:80，那么127.0.0.1就会把所有的0.0.0.0:80的数据拦截(
    # 因为127.0.0.1比0.0.0.0更特别)。
    # 解决方法为将端口绑定到具体IP
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 8081))

    tcp_server_socket.listen(128)

    while True:
        client_socket, client_addr = tcp_server_socket.accept()

        server_client(client_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()