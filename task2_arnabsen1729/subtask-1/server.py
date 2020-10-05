import socket
import sys

class Server:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        self.ADDR = ADDR
        self.DISCON_MSG = DISCON_MSG
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        self.SOCK.bind(self.ADDR)
        print(f'[SERVER STARTED] at {self.ADDR}...')
        self.SOCK.listen()
        return self.SOCK

    def accept_client(self):
        conn, addr = self.SOCK.accept()
        print(f'[NEW CONNECTION] Client {addr} added...')
        return conn, addr

    def recv_message(self, conn, CHUNKS=1024, FORMAT='utf-8'):
        data = conn.recv(CHUNKS).decode(FORMAT)
        print(f'[MESSAGE FROM {addr}] : \t{data}')
        if data=='':
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        return data
        
    def send_resp(self, conn, RESPONSE, FORMAT='utf-8'):
        print(f'[RESPONSE GIVEN by {self.ADDR}] : \t{RESPONSE}')
        conn.send(bytes(RESPONSE, FORMAT))


HOST = socket.gethostname()
PORT = 3033 # change this to any other available port
ADDR = (HOST, PORT)

server = Server(ADDR, '\x00')
server_sock = server.init()

while server_sock:
    conn, addr = server.accept_client()
    
    while True:
        data = server.recv_message(conn)
        server.send_resp(conn, data)