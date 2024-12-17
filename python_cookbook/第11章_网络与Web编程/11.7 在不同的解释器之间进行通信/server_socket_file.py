from multiprocessing.connection import Listener
import traceback


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(file_name, authkey):
    serv = Listener(file_name, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()


echo_server(r'\\.\pipe\test', authkey=b'peekaboo')
