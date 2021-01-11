import socket
import re
import select


def server_client(client_socket, request):
    request_lines = request.splitlines()
    print(request_lines)

    file = ''
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
        html_content = file.read()
        file.close()
        response_body = html_content

        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:{}\r\n'.format(len(response_body))
        response_header += '\r\n'
        response = response_header.encode('utf-8') + response_body
        client_socket.send(response)


def main():
    """用来完成整体控制"""

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(('', 8081))

    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建 epoll 对象 epoll 为 Linux 对象特有的 api,是多路 I/O 就绪通知方法，即时间通知方法。相较于以往的
    # for...in 的轮询(poll)方法 epoll 使用内存映射(mmap)技术，即一块内存，系统跟程序一起读(
    # 在本程序中，该内存存放了套接字的文件描述符)。
    # 当系统收到的数据是发往这个内存中的文件描述符，那么系统会通知程序去检查对应的内存中的文件描述符，这样提高了效率
    epl = select.epoll()  # 创建一个 epoll 对象
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)  # 把
    # tcp_server_socket 的fd注册到 epoll 中。其中  select.EPOLLIN 表示有数据到来

    fd_event_dict = dict()

    while True:
        fd_event_list = epl.poll()  # 默认会堵塞。直到 os 监测到有数据发送到 epoll 注册的fd，
        # 系统会通过 事件通知方式 告知程序并返回一个列表，同时解堵塞
        # 返回的列表的值为字典:
        # [(fd, event), (套接字对应的文件描述符, 文件描述符的时间，例如调用 receive 接收等)]

        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                client_socket, client_addr = tcp_server_socket.accept()
                epl.register(client_socket.fileno(), select.EPOLLIN)
                fd_event_dict[client_socket.fileno()] = client_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    server_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd_event_dict[fd])
                    del fd_event_dict[fd]


    tcp_server_socket.close()


if __name__ == '__main__':
    main()
