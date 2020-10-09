import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=(socket.gethostbyname(socket.gethostname()))
clientsocket.connect((ip,1234))
while True:
    print('Enter a message: ',end='')
    str=input()
    if str!='':
        clientsocket.send(str.encode());
    else:
        clientsocket.send(str.encode());
        print()
        print("Client terminated due to empty string")
        break
clientsocket.close()