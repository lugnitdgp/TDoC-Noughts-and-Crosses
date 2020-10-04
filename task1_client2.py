import socket
import sys
#creating socket to connect with other computers
host ='localhost'
port = 9999

command=input()
if command=='receive':
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("connect")
    s.connect((host,port))
    data = s.recv(8).decode() # this seems to be needed to first connect
    print("connected")

    while True:
        print('listening')
        s.setblocking(True)
        data = s.recv(1024).decode()
        print(data)
        
        print('input stuff please')
        data=input()
        if data=='quit' :
            s.close()
            break
        s.send(bytes(data,'utf-8'))

        
elif command=='send':
    
    def create_socket():
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print("socket creation error "+str(msg))

    #binding the socket and listening for connection
    def bind_socket(socket):
       try:
            print("binding the port "+str(port))
            socket.bind((host,port))
            socket.listen(5)
       except socket.error as msg:
            print("socket finding error "+str(msg)+"\n"+ "Retrying....")
            bind_socket()

    #establish connection with the client and the socket must be listening
    def socket_accept(socket):
        conn,address=socket.accept()
        print("Connection is established "+" IP  "+address[0]+" port  "+str(address[1]))
        send_commands(conn)
        conn.close()

    def send_commands(conn):
        conn.send(bytes('Welcome','utf-8'))
        while True:
            print('input stuff please')
            send_msg=input()
            conn.send(bytes(send_msg,'utf-8'))
            
            print('listening')
            msg=conn.recv(1024).decode()
            if msg=='quit':
                break
            print(msg)

            

    def main():
        socket = create_socket()
        bind_socket(socket)
        socket_accept(socket)

    main()
