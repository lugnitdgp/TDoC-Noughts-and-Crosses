import socket
import sys
import uuid
from gameLogic import TicTacToe


class Client:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        try:
            self.ID = uuid.uuid1()
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.DISCON_MSG = DISCON_MSG
            self.ADDR = ADDR
            self.SOCK.connect(ADDR)
            print(f'[CONNECTION SUCCESS] Connected to server {ADDR} ...')
        except:
            print('[SOMETHING WENT WRONG]...')
            sys.exit(0)
        

    def send_message(self, message, FORMAT='utf-8'):
        self.SOCK.sendall(bytes(message, FORMAT))
        if message == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        
    def recv_resp(self, CHUNKS=1024, FORMAT='utf-8'):
        data = self.SOCK.recv(CHUNKS).decode(FORMAT)
        # print(f'[RESPONSE FROM {self.ADDR}] : {data}')
        return data

    def assign_room(self, room_id):
        self.ROOM = room_id

    def send_creds(self):
        data = '{}#{}'.format(self.ROOM, self.ID).encode()
        self.SOCK.send(data)


HOST = socket.gethostname()
PORT = 3034 # change this to the port client1 is running
ADDR = (HOST, PORT)

client = Client(ADDR, 'Quit')
while True:
    roomId = input('[ENTER ROOM ID]: ')
    client.assign_room(roomId)

    # sending room id and uuid of the client 
    client.send_creds()
    id = client.recv_resp()
    if id=="FAILURE":
        print('[ROOM IS FULL]')
    else:
        print('YOU ARE PLAYER ', id)
        game=TicTacToe(int(id))
        break

while client.SOCK:
    if(game.id==1):
        # print('lll')
        p1_index = game.p1_move()
        print(f'[PLAYER 1 PLAYED]: {p1_index}')
        game.display_board()
        client.send_message(str(p1_index))
        if game.isGameOver(p1_index)!=0:
            print('[GAME OVER]')
            client.send_message('Quit')
            # client.SOCK.close()
            sys.exit(0)

        p2_index = int(client.recv_resp())
        game.p2_move(p2_index)
        game.display_board()
        print(f'[PLAYER 2 PLAYED]: {p2_index}')
        if game.isGameOver(p1_index)!=0:
            print('[GAME OVER]')
            client.send_message('Quit')
            # client.SOCK.close()
            sys.exit(0)
    else:
        
        p1_index = int(client.recv_resp())
        game.p1_move(p1_index)
        game.display_board()
        print(f'[PLAYER 1 PLAYED]: {p1_index}')
        if game.isGameOver(p1_index)!=0:
            print('[GAME OVER]')
            client.send_message('Quit')
            # client.SOCK.close()
            sys.exit(0)

        p2_index = game.p2_move()
        print(f'[PLAYER 2 PLAYED]: {p2_index}')
        game.display_board()
        client.send_message(str(p2_index))
        if game.isGameOver(p2_index)!=0:
            print('[GAME OVER]')
            client.send_message('Quit')
            # client.SOCK.close()
            sys.exit(0)
