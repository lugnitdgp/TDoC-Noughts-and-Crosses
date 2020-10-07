import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ""
port = 10000
s.bind((host,port))
s.listen(10)
conn, addr = s.accept()
print("someone  connected")
while True:
    msg = conn.recv(1024)
    if msg.decode('utf-8')!='exit':
        conn.send(str.encode("you are connected"))
    elif msg.decode('utf-8')=='exit':
        conn.send(str.encode("you connnection is lost"))
        break
s.close()
