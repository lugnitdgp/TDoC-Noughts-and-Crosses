
import socket

ip = '127.0.0.1'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))
print('socket connected')

while True:
    msg = input()

    if len(msg) > 0:
        s.sendall(msg.encode('utf-8'))
        print('message sent')
        a = s.recv(1024)
        b = a.decode('utf-8')
        print(b)
        print('message received')

    else:
        s.close()
        print('socket closed')
        break
