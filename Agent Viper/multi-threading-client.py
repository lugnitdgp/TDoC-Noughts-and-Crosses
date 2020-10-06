import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1234

s.connect((host, port))
message = s.recv(1024).decode('utf-8')
print(str(message))

while True:

    response = input('Say something => ')

    if response == '' or response == 'quit':
        s.close()
        print('Socket closed')
        break

    else:
        s.sendall(response.encode('utf-8'))
        print('Message Sent to Server')
