import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9090
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print("Conneted to :"+addr[0]+" "+str(addr[1])+"")
while True:
    msg = conn.recv(1024)
    if msg.decode("utf-8")=='quit':
        s.close()
        break
    print(msg.decode("utf-8"))
    conn.sendall(msg)
