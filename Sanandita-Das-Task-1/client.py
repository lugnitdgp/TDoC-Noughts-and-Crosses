import socket

HOST = '127.0.0.1'
PORT = 65432 #Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Enter your message (press enter to quit): ")
        s.sendall(bytes(msg, 'utf-8'))
        if not msg:
            break
        data = s.recv(1024)
        print('Received :', repr(data))
        if not data:
            break
