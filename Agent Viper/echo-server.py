import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

host = '127.0.0.1'
port = 1234

s.bind((host, port))
print('socket bound to port 6789')

s.listen(5)
print('socket is listening')

con, add = s.accept()
print('Connected to address ', add)

while True:
    message = con.recv(1024).decode('utf-8')
    print('message received')
    if len(message) > 0:
        con.send(str(message).encode('utf-8'))
        print('message sent')
    else:
        print('socket closed')
        con.close()
        s.close()
        sys.exit()
