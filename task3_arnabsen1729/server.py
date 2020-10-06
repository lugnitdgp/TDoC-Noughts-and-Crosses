import socket
import sys
from gameLogic import TicTacToe

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
        # print(f'[MESSAGE FROM {addr}] : {data}')
        if data == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        return int(data)
        
    def send_resp(self, conn, RESPONSE, FORMAT='utf-8'):
        conn.send(bytes(str(RESPONSE), FORMAT))


HOST = socket.gethostname()
PORT = 3033 # change this to any other available port
ADDR = (HOST, PORT)

p1 = Server(ADDR, 'Q')
server_sock = p1.init()
p1Game = TicTacToe(1)
print('[YOU ARE PLAYER 1]')
print('Waiting for opponent...')
while server_sock:
    conn, addr = p1.accept_client()
    print('[GAME STARTED]')
    while True:
        p1Move = p1Game.p1_move()
        p1Game.display_board()
        p1.send_resp(conn, p1Move)
        if p1Game.isGameOver(p1Move)!=0:
            conn.close()
            server_sock.close()
            sys.exit(0)
        print('Wait for PLAYER 2\'s move')
        p2Move = p1.recv_message(conn)
        print(f'[PLAYER 2 played]: {p2Move}')
        p1Game.p2_move(p2Move)
        p1Game.display_board()
        if p1Game.isGameOver(p2Move)!=0:
            conn.close()
            server_sock.close()
            sys.exit(0)