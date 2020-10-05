import socket

host = "127.0.0.1"
port = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        msg = input("> ")
        if not msg:
            s.send(str.encode(msg, "utf-8"))
            break
        else:
            s.send(str.encode(msg, "utf-8"))
            response = s.recv(1024)
            print(response.decode("utf-8"))
