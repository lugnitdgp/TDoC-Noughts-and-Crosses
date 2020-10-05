import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server any non privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data=input()         #input is taken by the client 
        if not data:
            break            #if no data input by the client then th while loop breaks
        s.sendall(bytes(data,'utf-8'))       #else the data is encoded and sent to the server
        data = s.recv(1024).decode()         #data that is receivd from server side is decoded

        print('Echoed-', repr(data))         #finally th echoed data is printed on the client side
