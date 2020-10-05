import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),10000))
#print(s.recv(1024).decode())
print(s.recv(1024).decode())


while True:
    data = input('>')
    s.send(str.encode(data))
    if data == '':
        print('bye..')
        s.close()
        sys.exit()
    print(s.recv(1024).decode('utf-8'))




