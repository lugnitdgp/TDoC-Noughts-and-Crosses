import socket
from _thread import start_new_thread
s = socket.socket()
s.bind(('', 12345))
s.listen()
def connection(c):
    c.send(str.encode("You've connected successfully!"))
    while True:
        data = str(c.recv(1024), "utf-8")
        if data == "!_quit_":
            c.send(str.encode("Closing connection..."))
            break
        c.send(str.encode(data))
    c.close()
while True:
    c, addr = s.accept()
    print("Connected to", addr)
    start_new_thread(connection, (c, ))
print("closing...")
s.close()