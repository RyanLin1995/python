import socket
import re
import multiprocessing


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

        p1 = multiprocessing.Process(target=server_client, args=(client_socket,))
        p1.start()

        # 在 Linux 中，把一切抽象为文件。例如显示器，键盘等均为文件。 因此，新接入一个外接设备或新建了一个网络接口后，Linux
        # 对应也会新建了一个特殊的文件，该文件的值称为 文件描述符 如显示器的文件描述符为1。 那么在程序新建了一个 socket 后，
        # Linux 底层就创建了一个有文件描述符的特殊文件，并把这个文件指向这个 socket
        # 然而多进程中，子进程会复制一份父进程的代码和资源，导致一个文件描述符指向了(通过了硬链接)两个 socket(父进程 socket 跟子进程
        # socket ) 那么在子进程中运行代码时，即使有 close 对象，那么也不会关闭该文件描述符(因为父进程还在打开)
        # 那么就要在父进程中添加 close，把得到的 socket 的文件描述符先关闭，交给 子进程去处理
        client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()