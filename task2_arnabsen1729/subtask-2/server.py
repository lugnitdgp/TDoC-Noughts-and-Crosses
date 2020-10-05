import socket
import sys
import threading

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

    def recv_message(self, conn, addr, CHUNKS=1024, FORMAT='utf-8'):
        data = conn.recv(CHUNKS).decode(FORMAT)
        print(f'[MESSAGE FROM {addr}] : \t{data}')
        return data
        
    def send_resp(self, conn, RESPONSE, FORMAT='utf-8'):
        print(f'[RESPONSE GIVEN by {self.ADDR}] : \t{RESPONSE}')
        conn.send(bytes(RESPONSE, FORMAT))

    def handle_client(self, conn, addr):
        while True:
            client_msg = self.recv_message(conn, addr)
            if client_msg == self.DISCON_MSG:
                print(f'[CLIENT LEFT] Client {addr} left server')
                break
            self.send_resp(conn, client_msg)

        try:
            # sometimes when the client closes the connection it errors out as BROKEN PIPE, so to avoid that we have used the try except block
            conn.close()
            return
        except:
            return
            


HOST = socket.gethostname()
PORT = 3034 # change this to any other available port
ADDR = (HOST, PORT)

server = Server(ADDR, 'Quit')
server_sock = server.init()

while server_sock:
    conn, addr = server.accept_client()
    t = threading.Thread(target=server.handle_client, args=(conn, addr))
    t.start()
    print(f'[ACTIVE CLIENTS] {threading.activeCount()-1}') 
    # reason of subtracting 1 is this loop is also a thread, so to get all the connections we have to subtract 1
    