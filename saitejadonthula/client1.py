import socket
import sys

s=socket.socket()
s.connect(("IP ADD",3456))
print('enter a message, write quit for exit !')

try:
    while True:
        data = input('>')
        s.send(str.encode(data))
        if data == "quit":
            s.close()
            sys.exit()
        #print('sent !')
        data = s.recv(1024).decode("utf-8")
        print(data)
        if data == "your friend's connection is lost :)":
            s.close()
            sys.exit()
except:
    print("connection lost")

    
