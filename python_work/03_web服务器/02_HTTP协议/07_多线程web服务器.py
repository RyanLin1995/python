import socket
import re
import threading


def server_client(client_socket):
    """为这个客户端返回数据"""
    request = client_socket.recv(1024).decode('utf-8')
    request_lines = request.splitlines()
    print(request_lines)

    try:
        # 要匹配的项为 GET /index.html HTTP/1.1
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'
            file = open('./html{}'.format(file_name), 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '-----Page not found -----'
        client_socket.send(response.encode('utf-8'))
        client_socket.close()
    else:
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        html_content = file.read()
        file.close()
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

        p1 = threading.Thread(target=server_client, args=(client_socket,))
        p1.start()

        # 而在多线程中不会复制父进程资源和代码，因此如果加上这句话，socket 会立马关闭，导致网页访问不了
        # client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()