import socket
import re
import multiprocessing
import sys
# import dynamic.mini_frame


class WSGIServer(object):

    def __init__(self, port, application, static):

        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(('', port))

        self.tcp_server_socket.listen(128)

        self.application = application

        self.static = static

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

        if not file_name.endswith(".html"):
            try:
                file = open('{}{}'.format(self.static, file_name), 'rb')
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

    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except:
            print("端口错误")
            return
    else:
        print("请按照以下方式输入")
        print("python3 web_server.py 7890 mini_frame:application")
        return

    result = re.match(r'([^:]+):(.*)', frame_app_name)

    if result:
        frame_name = result.group(1)
        application_name = result.group(2)

    else:
        print("请按照以下方式输入")
        print("python3 web_server.py 7890 mini_frame:application")
        return

    with open("web_server.cnf") as cnf:
        cnf_info = eval(cnf.read())

    static = cnf_info["static_path"]
    sys.path.append(cnf_info["dynamic_path"])

    frame = __import__(frame_name)

    app = getattr(frame, application_name)

    # print(app)

    wsgi_server = WSGIServer(port, app, static)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
