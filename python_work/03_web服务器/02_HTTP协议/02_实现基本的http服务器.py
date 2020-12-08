import socket


def server_client(client_socket):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求，即 http 请求
    # GET / HTTP/1.1
    request = client_socket.recv(1024)
    print(request)

    # 2. 返回 http 格式数据给浏览器
    # 2.1 准备发送给浏览器的数据---header
    response = 'HTTP/1.1 200 OK\r\n'  # 浏览器不能直接解析\n，要变为\r\n才可以(为了兼容 windows)
    response += '\r\n'  # 在 response 下加上空行
    # 2.2 准备发送给浏览器的数据---body
    response += '<h1>hahahahaha</h1>'
    client_socket.send(response.encode('utf-8'))

    # 关闭套接字
    client_socket.close()


def main():
    """用来完成整体控制"""

    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(('', 8081))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端链接
        client_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        server_client(client_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()