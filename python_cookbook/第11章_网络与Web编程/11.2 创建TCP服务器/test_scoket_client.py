from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 15000))
s.send(b'Hello\n')  # 发送带行分割符的数据
print(s.recv(8192))
