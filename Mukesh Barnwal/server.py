import socket        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
s.bind((HOST, PORT))      

print(f"[STARTING] starting server at {HOST}")

s.listen(1)
while True:    
    conn, addr = s.accept()
    print(f"[CONNECTED] connected with {addr}")
    msg = conn.recv(1024).decode('utf-8')
    if msg=='':
        break
    print(f"[{addr}] {msg}")
    print(f"[{HOST}] ")
    send_msg = input()

    # sendall() or send() functions are used for the stream socket or TCP
    # whereas sendto() is used for UDP
    conn.sendall(bytes(send_msg, 'utf-8'))

conn.close()
