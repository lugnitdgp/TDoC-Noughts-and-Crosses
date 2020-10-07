import socket
s = socket.socket()
host = socket.gethostname()
port = 9091

s.connect((host, 9090))

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    Input = input()
    if Input=='quit':
        s.close()
        break
    s.sendto(str.encode(Input),(host, 9090))
