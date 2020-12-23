import socket
import re
import multiprocessing
import sys
# import dynamic.mini_frame


class WSGIServer(object):

    def __init__(self, port, application):

        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(('', port))

        self.tcp_server_socket.listen(128)

        self.application = application

    def server_client(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        request_lines = request.splitlines()
        print(request_lines)

        # 要匹配的项为 GET /index.html HTTP/1.1
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])  # [^/]+ 表示匹配不是 / 的所有内容
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'

        if not file_name.endswith(".py"):
            try:
                file = open('./static{}'.format(file_name), 'rb')
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
        else:

            env = {"PATH_INFO": file_name}

            body = self.application(env, self.start_response)
            header = "HTTP/1.1 {}\r\n".format(self.status)

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header + body
            client_socket.send(response.encode('utf-8'))

        client_socket.close()

    def start_response(self, status, headers):

        self.status = status
        self.headers = [("Server", "mini_frame V8.8")]
        self.headers += headers

    def run_forever(self):

        while True:
            client_socket, client_addr = self.tcp_server_socket.accept()

            p1 = multiprocessing.Process(target=self.server_client, args=(client_socket,))
            p1.start()

            client_socket.close()

        self.tcp_server_socket.close()


def main():

    # 需要将端口以及框架在外部传入，实施的方式为 python3 web_server.py 7890 mini_frame:application
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # port
            frame_app_name = sys.argv[2]  # 框架跟应用程序名字
        except:
            print("端口错误")
            return
    else:
        print("请按照以下方式输入")
        print("python3 web_server.py 7890 mini_frame:application")
        return

    # 要匹配的字段为 mini_frame:application
    result = re.match(r'([^:]+):(.*)', frame_app_name)

    if result:
        frame_name = result.group(1)  # 框架名
        application_name = result.group(2)  # 框架内应用名

    else:
        print("请按照以下方式输入")
        print("python3 web_server.py 7890 mini_frame:application")
        return

    # 得到框架名跟应用名后，需要更改import的路径，将 dynamic 加到 import 搜索路径中
    sys.path.append("./dynamic")

    # 此时不能通过 import frame_name 直接导入，因为 import 会认为导入的是名为 frame_name.py 的文件。而不是最终想要的 mini_frame.py
    # 因此可以使用 __import__() 函数，该函数的返回值标记着要导入的模块
    frame = __import__(frame_name)

    # 有了要导入的实际函数 frame 后，可以用getattr()函数从 frame 中获取 application_name 函数，在这里获得的是 mini_frame.application
    app = getattr(frame, application_name)

    # print(app)

    wsgi_server = WSGIServer(port, app)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
