import socket                   # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

s.connect((socket.gethostbyname(socket.gethostname()), 50000))

while True:
    msg = input()
    s.sendall(bytes(str(len(msg)), 'utf-8'))
    if(msg==''):
        break
    s.send(msg.encode('utf-8'))
    sent = s.recv(1024).decode('utf-8')
    print(f"Server response : {sent}")
s.close()
print('connection closed')