import socket
import sys

s=socket.socket()
s.connect((gethostname(),10000))
print('''--enter msg only after'>' 
         --enter quit to exit !''')
try:
    while True:
        data=s.recv(1024).decode("utf-8")
        print(data)
        if data=="your friend's connection is lost :)":
            s.close()
            sys.exit()
        data = input('>')
        s.send(str.encode(data))
        if data == "quit":
            s.close()
            sys.exit()
except:
    print("connection lost")
