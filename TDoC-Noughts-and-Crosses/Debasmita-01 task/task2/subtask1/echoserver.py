import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a socket instance and passed in two parameters
host='127.0.0.1'
port=12345 #reserving a port 
s.bind((host,port))
s.listen(5) # listening mode
dsend=''

while True:  # an infinite loop until interrupted 
   c, addr = s.accept()      # Establish connection with client. 
   print ('Got connection from', addr )
   
   while True:
       data=c.recv(1024).decode() # decoding the received data
       print("Message successfully received")
       if data=='':
           ("Nothing received,Connection closed")
           break
   c.close()

