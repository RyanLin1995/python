import socket


def send_file(client_socket, client_add):

    # 接收文件名
    file_name = client_socket.recv(1024).decode("utf-8")
    print("Send {} to {}".format(file_name, client_add))

    # 打开文件
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except:
        print("No this file: {}".format(file_name))

    # 发送文件数据
    if file_content:
        client_socket.send(file_content)


def main():

    # 1. 创建套接字
    tcp_server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本机信息
    tcp_server_client.bind(('', 7890))

    # 3. 把socket从主动变被动
    tcp_server_client.listen(128)  # 简单理解为可以同一时刻链接的客户端数字，但是不同操作系统有不同的处理方式

    while True:
        # 4. 等待客户端链接
        client_socket, client_add = tcp_server_client.accept()

        # 5. 发送文件
        send_file(client_socket, client_add)

        # 6. 关闭客户端socket
        client_socket.close()

    # 7. 关闭服务器socket
    tcp_server_client.close()


if __name__ == '__main__':
    main()