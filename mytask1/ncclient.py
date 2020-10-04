import socket
  
s = socket.socket()   # Create a socket object
port = 12345    # port which we want to connect
s.connect(('127.0.0.1', port))
while True:
    print('Type your message')
    msg=input()
    msg.upper()
    s.send(msg.encode())
    if(msg=="quit"):
        break
    print ("Response received",s.recv(1024).decode())
s.close()
