import socket
import sys
import ttg
host = socket.gethostname()  
port = 8000  # socket server port number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # instantiate
sock.connect((host, port))  # connect to the server

print("Running on ", host, port)
print("Player 2")
mesg = input("-> ")  # take input

while True:

    # print("Sending..:",mesg)

    
    sock.send(str(mesg).encode('utf-8'))
    received_mesg = sock.recv(1024).decode('utf-8')
    # print(received_mesg)
    if(mesg == "0" or received_mesg == "0"):
        sock.close()
        sys.exit()
        print("Quiting..")
        # print("recived mesg:",  received_mesg)
        break
    while(received_mesg == "repeat"):
        print("Choose again!!..")
        mesg = input()
        sock.send(str(mesg).encode('utf-8'))
        received_mesg = sock.recv(1024).decode('utf-8')


    mesg = input("-> ")  # take input

sock.close()  # close the connection







