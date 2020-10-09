import socket
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostbyname(socket.gethostname()) , 1234))
serversocket.listen(5)
sendData=''
while True:
    c,addr=serversocket.accept()
    print("Success connection from ", addr)
    while True:
        rcvdData = c.recv(1024).decode()
        print ("Message received from client: ",rcvdData)
        if rcvdData=='':
            print('Empty string received. End of connection')
            break
    c.close()

