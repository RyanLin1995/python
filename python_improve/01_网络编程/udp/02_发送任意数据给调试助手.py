import socket


def main():
    # 创建一个远端udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")

    # 可以使用套接字收发数据
    # udp_socket.sendto(b"hahahahaha1", ('192.168.1.11', 1357))
    udp_socket.sendto(send_data.encode('utf-8'), ('192.168.1.6', 1357))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
