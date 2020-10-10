import socket
import pygame
import time
from grid import Grid
import threading

pygame.init()

# To fixed the position of the window
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '10,20'

# gui using pygame
surface = pygame.display.set_mode((470, 520))
pygame.display.set_caption('Tic-Tac-Toe')
run = True
grid = Grid()
turn = 0
x, y, res = None, None, None
player = 'X'

# Defining socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
FORMAT = 'utf-8'
s = socket.socket()
s.bind((HOST, PORT))
print('[STARTED] server started.')
s.listen(1)
print(f'[LISTENING] server is listening on {HOST}')

conn, addr = None, None
connected = False
listening = 1


def connect_with_client():
    global connected, conn, addr    
    conn, addr = s.accept()
    connected = True
    print(f'[CONNECTED] connected with {addr}')
    recv_msg()

def start_thread(target):
    thread = threading.Thread(target=target, daemon=True)
    thread.start()

def recv_msg():
    global x, y, turn, conn, listening, connected
    while True:
        msg = conn.recv(1024).decode(FORMAT)
        #print(msg)
        if msg=='quit':
            grid.clear()
            connected = False
            listening = 1
            break
        else:
            data = msg.split('-')
            x, y = int(data[0]), int(data[1])
            grid.set_cell_value(x, y, 'O')
            turn^=1
    conn.close()
    print('quit')
    

while run:
    header = 'WAITING FOR CONNECTION'
    surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over and connected:
            if pygame.mouse.get_pressed()[0]==1 and turn==0:
                pos = pygame.mouse.get_pos()
                x, y = (pos[0]-10)//150, (pos[1]-60)//150  
                flag = grid.set_cell_value(x, y, player)
                if flag:        
                    msg = "{}-{}".format(x, y).encode(FORMAT)
                    conn.send(msg)              
                    turn ^= 1
    if not connected:
        grid.write_text(header, 235, 260, surface, 26)
        if listening==1:
            start_thread(connect_with_client)
            listening -= 1
    elif grid.game_over:
        if res==None:
            header = 'GAME OVER!'
        elif res==player:
            header = 'YOU WIN'
        else:
            header = 'PLAYER O WIN'
        grid.write_text(header, 235, 260, surface, 50)
        grid.button(surface, 'RESTART', 160, 380, 150, 70, (0,200,0), (0,255,0))
    else:
        header = 'Your Turn' if turn==0 else "Player O's Turn"
        grid.write_text(header, 235, 25, surface, 25)
        grid.draw_sign(surface)
        grid.draw_line(surface)        
        if grid.cnt==1:
            res = grid.check()
            if grid.game_over:
                if res is not None:
                    print(f'Player {res} win.')
                else:
                    print('Game over!')
                grid.update(surface, header)
                time.sleep(2)

    pygame.display.update()
    