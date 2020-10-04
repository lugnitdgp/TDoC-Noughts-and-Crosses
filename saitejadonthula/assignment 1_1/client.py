import socket
import sys
y=input('enter 1 if you are client 1 else 2 if you are 2nd client : ')
s = socket.socket()
if y=='1':
    s.connect((socket.gethostname(), 3456))
    print(s.recv(1024).decode())
    print(s.recv(1024).decode())
    print('enter a message, write quit for exit !')

    try:
        while True:
            data = input('>')
            s.send(str.encode(data))
            if data == "quit":
                s.close()
                sys.exit()
            # print('sent !')
            data = s.recv(1024).decode("utf-8")
            print('       <'+data)
            if data == "your friend's connection is lost :)":
                s.close()
                sys.exit()
    except:
        print("connection lost")
else:
    s.connect((socket.gethostname(), 10000))
    print('''--enter msg only after'>' 
--enter quit to exit !''')
    try:
        while True:
            data = s.recv(1024).decode("utf-8")
            print('       <'+data)
            if data == "your friend's connection is lost :)":
                s.close()
                sys.exit()
            data = input('>')
            s.send(str.encode(data))
            if data == "quit":
                s.close()
                sys.exit()
    except:
        print("connection lost")


