import socket
import sys
host = socket.gethostname()  
port = 8000  # socket server port number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # instantiate
sock.connect((host, port))  # connect to the server

print("Running on ", host, port)
mesg = input(" -> ")  # take input

while True:

    print("Sending..:",mesg)

    
    sock.send(str(mesg).encode('utf-8'))
    received_mesg = sock.recv(1024).decode('utf-8')
    if(mesg == "" or received_mesg == ""):
        sock.close()
        sys.exit()
        print("Quiting..")
        print("recived mesg:",  received_mesg)
    mesg = input(" -> ")  # take input

sock.close()  # close the connection







