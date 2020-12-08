import socket
import threading


def rece_msg(udp_socket):
    """接收信息"""

    while True:
        rece_data = udp_socket.recvfrom(1024)
        print("{}:{}".format(rece_data[1], rece_data[0].decode('utf-8')))


def send_msg(udp_socket, dest_ip, dest_port):

    while True:
        send_data = input("请输入要发送的内容: ")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():

    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 信息
    addr = ('', 7890)
    dest_ip = input("请输入对方IP: ")
    dest_port = int(input("请输入对方Port: "))

    # 3. 绑定
    udp_socket.bind(addr)

    # 接收信息
    t_rece = threading.Thread(target=rece_msg, args=(udp_socket,))

    # 发送信息
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_rece.start()
    t_send.start()


if __name__ == '__main__':
    main()