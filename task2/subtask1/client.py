import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9091
s.connect((host, 9090))
while True:
    Input = input("Enter anything : ")
    s.sendto(str.encode(Input), (host, 9090))
    if Input == 'quit':
        s.close()
        break
    res = s.recv(1024)
    print(res.decode('utf-8'))
