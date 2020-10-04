import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024).decode()
    if data == 'Ping':
        msg="Pong"
        s.sendto(msg.encode(),(HOST,PORT))
        print("send client_1",msg)
    
    print('Received : {}'.format(data))
