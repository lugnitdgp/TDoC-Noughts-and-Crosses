 
import socket
import sys
from gameLogic import TicTacToe


class Client:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        try:
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.DISCON_MSG = DISCON_MSG
            self.ADDR = ADDR
            self.SOCK.connect(ADDR)
            print(f'[NEW CONNECTION] Client {ADDR} added...')
        except:
            print('[SOMETHING WENT WRONG]...')
        

    def send_message(self, message, FORMAT='utf-8'):
        self.SOCK.sendall(bytes(str(message), FORMAT))
        if message == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        
    def recv_resp(self, CHUNKS=1024, FORMAT='utf-8'):
        data = self.SOCK.recv(CHUNKS).decode(FORMAT)
        # print(f'[RESPONSE FROM {self.ADDR}] : {data}')
        return int(data)

HOST = socket.gethostname()
PORT = 3033 # change this to the port client1 is running
ADDR = (HOST, PORT)

p2 = Client(ADDR, 'Q')
p2Game = TicTacToe(2)
print('[YOU ARE PLAYER 2]')
print('[GAME STARTED]')
while p2.SOCK:
    print('Wait for PLAYER 1\'s move')
    p1Move = p2.recv_resp()
    print(f'[PLAYER 1 played]: {p1Move}')
    p2Game.p1_move(p1Move)
    p2Game.display_board()
    if p2Game.isGameOver(p1Move)!=0:
            p2.SOCK.close()
            sys.exit(0)
    
    p2Move = p2Game.p2_move()
    p2Game.display_board()
    p2.send_message(p2Move)
    if p2Game.isGameOver(p2Move)!=0:
        p2.SOCK.close()
        sys.exit(0)