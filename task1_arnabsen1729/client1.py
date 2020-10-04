import socket
import sys

class Server:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        self.ADDR = ADDR
        self.DISCON_MSG = DISCON_MSG
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        self.SOCK.bind(self.ADDR)
        self.SOCK.listen()
        return self.SOCK

    def accept_client(self):
        conn, addr = self.SOCK.accept()
        print(f'[NEW CONNECTION] Client {addr} added...')
        return conn, addr

    def recv_message(self, conn, CHUNKS=1024, FORMAT='utf-8'):
        data = conn.recv(CHUNKS).decode(FORMAT)
        print(f'[MESSAGE FROM {addr}] : {data}')
        if data == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        return data
        
    def send_resp(self, conn, RESPONSE='PONG', FORMAT='utf-8'):
        print(f'[RESPONSE GIVEN {self.ADDR}] : {RESPONSE}')
        conn.send(bytes(RESPONSE, FORMAT))


HOST = socket.gethostname()
PORT = 3033 # change this to any other available port
ADDR = (HOST, PORT)

client = Server(ADDR, 'Q')
client_sock = client.init()

while client_sock:
    conn, addr = client.accept_client()
    
    while True:
        data = client.recv_message(conn)
        if data == 'PING':
            client.send_resp(conn)
        else:
            client.send_resp(conn, 'Hello there!')
