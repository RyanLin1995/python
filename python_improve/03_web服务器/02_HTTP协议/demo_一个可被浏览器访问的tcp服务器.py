import socket


def html_info():

    info = """HTTP/1.1 200 OK

    <h1>hahahahaha</h1>
    """

    return info


def main():

    # 创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP和端口
    tcp_socket.bind(('192.168.1.11', 8081))

    # 让socket从被动变为主动
    tcp_socket.listen(128)

    while True:
        # 等待客户端链接
        client_socket, client_addr = tcp_socket.accept()

        # 持续接收客户端发送来的消息
        while True:
            rece_info = client_socket.recv(1024)

            print(rece_info.decode('utf-8'))

            if rece_info:
                html = html_info()
                client_socket.send(html.encode('utf-8'))

            else:
                break
        # 关闭客户端socket，意味着不再为这个客户端服务
        client_socket.close()

    tcp_socket.close()


if __name__ == '__main__':
    main()