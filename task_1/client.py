import socket
s = socket.socket()
host = "192.168.137.1"
port = 10000
s.connect((host,port))
while True:
    msg = str(input())
    s.send(str.encode(msg))
    data = s.recv(1024)
    recieve = data.decode('utf-8')
    if recieve=='exit':
        break
s.close()
