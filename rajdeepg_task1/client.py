import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=(socket.gethostbyname(socket.gethostname()))
clientsocket.connect((ip,1234))
while True:
    print('Enter a msg',end='')
    str=input()
    str.upper()
    clientsocket.send(str.encode());
    if(str == "BYE" or str == "bye"):
        break
    print ("Response received",clientsocket.recv(1024).decode())
clientsocket.close()