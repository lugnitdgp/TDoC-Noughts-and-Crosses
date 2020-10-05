import socket
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
print(str(s.recv(1024), "utf-8"))
while True:
    message = input(">>")
    if message == '':
        s.send(str.encode("!_quit_"))
        break
    s.send(str.encode(message))
    print(str(s.recv(1024), "utf-8"))
print("Closing...")
s.close()
