import socket


def main():

    # 1. 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的ip port
    server_add = input("请输入服务器的ip: ")
    server_port = int(input("请输入服务器端口: "))

    # 3. 链接服务器
    tcp_client_socket.connect((server_add, server_port))

    # 4. 获取下载文件的名字
    file_name = input("请输入文件名: ")

    # 5. 发送下载文件名字到服务器
    tcp_client_socket.send(file_name.encode("utf-8"))

    # 6. 接受文件中的数据
    file_data = tcp_client_socket.recv(1024)  # 1024=1k, 1024*1024=1M

    if file_data:
        # 7. 保存数据到一个文件中
        with open("[新]{}".format(file_name), "wb") as f:  # wb为二进制模式写入
            f.write(file_data)

    # 8. 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()