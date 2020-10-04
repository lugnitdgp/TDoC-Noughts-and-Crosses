import socket                   # Import socket module

c = socket.socket()       

s.connect((socket.gethostname(), 50001))
msg = input()
s.send(bytes(msg, 'utf-8'))
data = s.recv(1024)
print('client received', data.decode('utf-8'))
s.close()
print('connection closed')