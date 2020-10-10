import socket        
import threading

HEADER = 64
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
s.bind((HOST, PORT))      

def handle_client(conn, addr):
    while True:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        if msg_length<=0:
            break
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        conn.send("Message Received".encode(FORMAT))
    
    conn.close()
    print("Connection closed.")
    

def start():
    s.listen()
    print(f"[LISTENING] Server listening on {HOST}")
    while True:
        conn, addr = s.accept()
        print(f"[CONNECTED] connected with {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}") # one thread is running that is our main program
        
print("[STARTING] server started...")
start()