import socket
import sys

host = '127.0.0.1'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket successfully created')
s.bind((host, port))
print('socket bind to port 1234')
s.listen(5)
print('socket is listening')
conn, address = s.accept()
print('Connected')
print('address ',address)
while True:
    received_msg = str(conn.recv(1024), 'utf-8')
    if received_msg == 'ping':
        conn.send(b'pong')
        print('data sent')
    elif received_msg == '' or received_msg == 'quit':
        conn.close()
        s.close()
        sys.exit()

    else:
        continue
