import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
FORMAT = 'utf-8'

s = socket.socket()

s.connect((HOST, PORT))

while True:
    msg = input()
    s.send(msg.encode(FORMAT))
    if msg=='quit':
        break
    msg = s.recv(1024).decode(FORMAT)
    print(msg)

s.close()