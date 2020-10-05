import socket
s = socket.socket()
host = socket.gethostname()
port = 9090

s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print("connected to "+addr[0]+" "+str(addr[1])+"")
while True:
    Input = input()
    if Input=='quit':
        s.close()
        break
    conn.send(str.encode(Input))
    res = conn.recv(1024)
    print(res.decode("utf-8"))
