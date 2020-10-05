import socket

# Creating Socket And Defining Host and Port Name
s = socket.socket()
host = socket.gethostbyname('localhost')
port = 9999

# Establishing Connection
s.connect((host, port))

# The Main Program Goes Here i.e. Sends A message And Recieves The Echoed Message and prints it
while True:
    print("Enter The Message : ", end="")
    data = input()
    if(data == ''):
        s.sendall(b'\x00')
    else:
        s.sendall(data.encode("utf-8"))
    msg = s.recv(1024)
    if msg == b'\x00':
        break
    print("Recieved : ", end="")
    print(msg.decode("utf-8"))
