import socket

HOST_ID = '127.0.0.1'
PORT_ID = 34625

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_ID, PORT_ID))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connection done', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)