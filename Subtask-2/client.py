# Import socket module 
import socket 


def Main():
    
    # local host IP '127.0.0.1' 
    host = 'localhost'

    # Define the port on which you want to connect 
    port = 9999

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    # connect to server on local computer 
    s.connect((host,port)) 

    # message you send to server 
    
    while True:
        print("Enter a message:")
        message =input()
        if not message:
            break
        # message sent to server 
        s.send(bytes(message,'utf-8')) 

        # messaga received from server
        
        data = s.recv(1024).decode()
        print("You sent the message-->")
        # print the received message 
       
        #'Received from the server :',echo
        print(data) 

        
    s.close() 

if __name__ == '__main__': 
	Main() 
