import socket
import sys

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 127.0.0.1,==
ip = socket.gethostname()
port=8001
sock.bind((ip, port))
print("Running on ", ip, port)

count = 0
while True:
    received_mesg = sock.recv(1024).decode('utf-8')
    
    if received_mesg == "ping":
        sock.sendto(str("pong").encode('utf-8'), (ip, 8000))
        print("sending:",  "pong")
    if (received_mesg == "quit"):
        print("Quiting..")
        sock.sendto(str("quit").encode('utf-8'), (ip, 8000))
        sock.close()
        sys.exit()
        break
    sock.sendto(str("not Pong 😅").encode('utf-8'), (ip, 8000))
    print(received_mesg)






