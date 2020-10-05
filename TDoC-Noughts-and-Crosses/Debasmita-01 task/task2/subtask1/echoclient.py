import socket
  
s = socket.socket()   # Create a socket object
port = 12345    # port which we want to connect
s.connect(('127.0.0.1', port))
while True:
    print('Type your message')
    msg=input()
    msg.upper()
    if msg !='':
        s.send(msg.encode())
    else:
        s.send(msg.encode())
        print("Connection ended")
        break
    
s.close()
