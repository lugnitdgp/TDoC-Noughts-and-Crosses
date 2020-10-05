import socket

host = "127.0.0.1"
port = 9998

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    print(f'Connection established. | IP: {addr[0]} | Port: {addr[1]}')
    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        else:
            conn.send(msg)