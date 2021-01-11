import socket
import re


def server_client(client_socket):
    """为这个客户端返回数据"""
    # 整体思路:
    # 1. 用正则表达式获取需要访问的文件名
    # 2. 查找文件名，如果存在就打开并作为body传回给客户端。不存在就回送错误信息
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

        server_client(client_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()