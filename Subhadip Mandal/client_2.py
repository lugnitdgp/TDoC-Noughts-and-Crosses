import socket

host = "127.0.0.1"
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print('''
Conversation started. Send message and wait for reply.
To end conversation send: "quit".
''')

while True:
    data = s.recv(1024)
    if data.decode("utf-8") == 'quit':
        s.send(str.encode('quit'))
        s.close()
        break
    else:
        print(f'received: {data.decode("utf-8")}')
        response = str.encode(input('send: '))
        if response.decode("utf-8") == 'quit':
            s.send(response)
            break
        else:
            s.send(response)