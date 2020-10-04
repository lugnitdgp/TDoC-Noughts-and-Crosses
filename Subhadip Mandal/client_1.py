import socket

host = "127.0.0.1"
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
connection, address = s.accept()

print(f'''
Connection established. | IP: {address[0]} | Port: {address[1]}

Conversation started. Send message and wait for reply.
To end conversation send: "quit".

''')

while True:
    data = str.encode(input('send: '))
    connection.send(data)
    client_response = (connection.recv(1024))
    if client_response.decode("utf-8") == 'quit':
        connection.close()
        s.close()
        break
    else:
        print(f'received: {client_response.decode("utf-8")}')