import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
FORMAT = 'utf-8'

s = socket.socket()
s.bind((HOST, PORT))

print('[STARTED] server started')
s.listen(3)

print(f'[LISTENING] server is listening on {HOST}')

while True:
    conn, addr = s.accept()
    print(f'[CONNECTED] connected with {addr}')
    while True:
        msg = conn.recv(1024).decode(FORMAT)
        print(msg)
        if msg=='quit':
            conn.close()
            break
        else:
            conn.send(msg.encode(FORMAT))