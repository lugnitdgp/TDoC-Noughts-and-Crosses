import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1234
s.connect((host, 1233))

response = s.recv(1024)
print(response.decode("utf-8"))

while True:
    Input = input()
    if Input == 'quit':
        s.sendall(str.encode(Input))
        s.close()
        break
    s.sendall(str.encode(Input))
