from multiprocessing.connection import Client

c = Client(r'\\.\pipe\test', authkey=b'peekaboo')
c.send('hello')
print(c.recv())
