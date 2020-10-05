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
        print ("Msg received",rcvdData)
        if rcvdData=='PING':
            sendData = "PONG"
        elif rcvdData=='PONG':
            sendData='PING'
        print('Response sent',sendData)
        c.send(sendData.encode())
        if(sendData == "BYE" or sendData == "bye"):
            break
    c.close()

