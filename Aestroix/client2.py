# IT'S YOUR FRIEND WORK IF THE CLIENT1 IS LISTENING


import socket


s = socket.socket()
host = "172.20.10.2" 


'''
THIS IS THE IP ADDRESS OF THE HOST. IN OUR CASE WE HAVE USED THE IP ADDRESS EXPLICITLY.

ONCE THE VM IS READY AND HOST IS PLACED THERE, THE IP ADRESS OF THE SERVER WILL GO IN HERE AS IT WILL BE STATIC

'''


port = 9998  # Port to listen on (non-privileged ports are > 1023)

s.connect((host, port)) # binding the socket in client file

while True:
    #RECEIVING DATA FROM SERVER FILE AND DECODING IT
    data = s.recv(1024).decode('utf-8')

    if data == 'quit':
        print("exiting>>>")

        # shutting down read and write closes all connections with all the channels that use this port. In our case its one so omitting it will work fine
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        break
    
    elif data == "ping":
        s.send(str.encode('pong :)', 'utf-8'))
        print("pong...")
