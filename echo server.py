import socket
import sys

host = socket.gethostname()
port = 8000  # initiate port no above 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # get instance
# The bind() host & port
server_socket.bind((host, port)) 

# configure how many client the server can listen simultaneously
server_socket.listen(1)
conn, address = server_socket.accept()  # accept new connection it would not work without listen fn
print("Connection from: " + str(address))
while True:
    data = conn.recv(1024).decode('utf-8')
    if data == "":
        break
    print("from connected user: " + str(data))
    conn.send((data+" 🥰 ").encode('utf-8'))  # send data to the client
conn.close()  # close the connection