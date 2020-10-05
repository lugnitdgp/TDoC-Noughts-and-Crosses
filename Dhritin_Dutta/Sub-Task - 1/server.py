import socket
s = socket.socket()
s.bind(('', 12345))
s.listen()
c, addr = s.accept()
print("Connected to", addr)
while True:
    message = str(c.recv(1024), "utf-8")
    if message != "!quit":
        print("Received :", message)
        c.send(str.encode(message, "utf-8"))
    else:
        print("Received :", '')
        c.send(str.encode("Closing connection..."))
        print("Closing...")
        break
s.close()       