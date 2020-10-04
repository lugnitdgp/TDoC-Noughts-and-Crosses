import socket

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 9999

s.connect((host, port))
data = s.recv(1024)
print(data.decode("utf-8"))
print("[Type Quit To Exit !]")

while True:
    data = s.recv(1024)
    data = data.decode("utf-8")
    if(data.lower() == 'client1>>> quit'):
        s.close()
        break
    if(data.lower() == 'client1>>> ping'):
        print(data)
        s.send(str.encode("Client2>>> Pong", "utf-8"))
        print("Client2>>> Pong")
        continue
    print(data)
    print("Client2>>> ", end="")
    chat = input()
    chat = "Client2>>> " + chat
    s.send(str.encode(chat, "utf-8"))
    if(chat.lower() == 'client2>>> quit'):
        s.close()
        break
