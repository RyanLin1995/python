import socket
import time


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 8081))

    tcp_server_socket.listen(128)

    tcp_server_socket.setblocking(False)  # 把TCP服务器套接字设置为非堵塞

    client_socket_list = list()

    while True:

        time.sleep(1)

        try:
            client_socket, client_addr = tcp_server_socket.accept()
        except:
            print('---没有客户端到来---')
        else:
            print('---来了一个新的客户端---')
            client_socket.setblocking(False)  # 把客户端套接字设置为非堵塞，但是设置为非堵塞之后，如果没有任何链接到来会出现错误，因此需要用try
            client_socket_list.append(client_socket)

        for client_new_socket in client_socket_list:
            try:
                recv_data = client_new_socket.recv(1024)
            except:
                print('---没有数据到来---')
            else:
                print(recv_data)
                if recv_data:
                    # 对方发送了数据，服务器处理
                    print('---数据来了---')
                else:
                    # 对方调用了close，服务器同样调用close
                    client_new_socket.close()
                    client_socket_list.remove(client_new_socket)
                    print('客户端已关闭')

    tcp_server_socket.close()


if __name__ == '__main__':
    main()