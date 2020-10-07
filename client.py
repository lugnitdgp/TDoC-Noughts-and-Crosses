import socket
import sys
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 127.0.0.1,==
ip = socket.gethostname()
port=8000
sock.bind((ip, port))
print("Running on ", ip, port)

while True:
    mesg = input()
    print("Sending..:",mesg)

    
    sock.sendto(str(mesg).encode('utf-8'), (ip,8001))
    received_mesg = sock.recv(1024).decode('utf-8')
    if(mesg == "quit" or received_mesg == "quit"):
        sock.close()
        sys.exit()
        print("Quiting..")
    print("recived mesg:",  received_mesg)







