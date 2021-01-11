import socket
import time

def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('', 1357))
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 连接服务器
    server_ip = input("请输入IP：")
    server_port = int(input("请输入port："))
    server_add = (server_ip, server_port)
    tcp_socket.connect(server_add)

    # 3. 发送数据
    # send_data = input("请输入要发送的消息：")
    send_data = "GET / HTTP/1.1\r\n"
    send_data += 'Host: 192.168.1.11:8081\r\n'
    send_data += 'Connection: keep-alive\r\n'
    send_data += 'Upgrade-Insecure-Requests: 1\r\n'
    send_data += 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36\r\n'
    send_data += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    send_data += 'Referer: http://192.168.1.11:8081/tutorial.html\r\n'
    send_data += 'Accept-Encoding: gzip, deflate\r\n'
    send_data += 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'

    while True:
        # tcp_socket.send(send_data.encode("utf-8"))
        tcp_socket.send(send_data.encode("utf-8"))
        time.sleep(0.1)

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()