
# The server does not stop listening even after client program has finished

import socket

s = socket.socket()

port = 1234

s.connect(('127.0.0.1', port))

while True:
    p = input()

    if p == 'ping':
        arr = p.encode('utf-8')
        s.send(arr)
        print(end='')
        a = s.recv(1024)
        b = a.decode('utf-8')
        print(b)

    elif p=='' or p=='quit':
        arr = p.encode('utf-8')
        s.send(arr)
        break

    else:
        continue

