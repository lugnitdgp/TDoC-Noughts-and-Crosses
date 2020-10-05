import socket

HOST = '127.0.0.1'
PORT = 65432 #Prt to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Listening on ", PORT, "\n")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("Received:", repr(data))
            if not data:
                break
            msg = input("Enter your message (press enter to quit): ")
            conn.sendall(bytes(msg, 'utf-8'))
            if not msg:
                break
