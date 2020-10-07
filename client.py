import socket

HOST_ID = '127.0.0.1'
PORT_ID = 34625

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_ID, PORT_ID))
    s.sendall(b'Hi to all ')
    data = s.recv(1024)

print('Received', repr(data))