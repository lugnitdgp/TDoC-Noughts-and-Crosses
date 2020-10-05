# Python TCP Client A
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000
print("tcpClientA: Enter message/ Enter exit:") 
MESSAGE = input() 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode())     
    print("tcpClientA: Enter message to continue/ Enter exit:")
    MESSAGE = input()

tcpClientA.close() 