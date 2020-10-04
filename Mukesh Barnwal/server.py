import socket        

s = socket.socket()             
s.bind((socket.gethostname(), 50001))          
s.listen(5)                    

print('Server listening....')

#waiting for Infinite time

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('connected with', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    print('Done sending')
    conn.send(bytes('Thank you for connecting', 'utf-8'))
    conn.close()