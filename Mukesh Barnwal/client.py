import socket
import pygame
import time
from grid import Grid
import threading

pygame.init()

# To fixed the position of the window
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '650,20'

# gui using pygame
surface = pygame.display.set_mode((470, 520))
pygame.display.set_caption('Tic-Tac-Toe')
run = True
grid = Grid()
turn = 0
x, y, res = None, None, None
player = 'O'

# Defining socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50000
FORMAT = 'utf-8'
s = socket.socket()
recv = True
username, opponent = '', ''
connected, username_take_time = False, 1
win, lose = 0, 0

def recv_msg():
    global x, y, turn, opponent 
    s.connect((HOST, PORT))
    s.send(username.encode(FORMAT))
    opponent = s.recv(1024).decode(FORMAT)
    turn, win, lose = 0, 0, 0
    while recv:
        msg = s.recv(1024).decode(FORMAT)
        #print(msg)        
        if len(msg)==3:
            data = msg.split('-')
            x, y = int(data[0]), int(data[1])
            grid.set_cell_value(x, y, 'X')
            turn^=1

def start_thread(target):
    thread = threading.Thread(target=target, daemon=True)
    thread.start()
  
inputRect = pygame.Rect(85, 317, 300, 34)
inputactive = False

def quitgame():
    s.send('quit'.encode(FORMAT))
    #pygame.quit()
    quit()

while run:
    header = 'Enter the username'
    surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame()
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over and connected:
            if pygame.mouse.get_pressed()[0]==1 and turn==1:
                pos = pygame.mouse.get_pos()
                x, y = (pos[0]-10)//150, (pos[1]-60)//150 
                flag = grid.set_cell_value(x, y, player)
                if flag:        
                    msg = "{}-{}".format(x, y).encode(FORMAT)
                    s.send(msg)              
                    turn ^= 1    
        if event.type == pygame.KEYDOWN and inputactive:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                pass
            elif event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                inputactive = True
    if not connected or username_take_time==1:
        grid.write_text(surface, header, 235, 260, 26)
        if username_take_time==1:            
            enter = grid.input_box(surface, username, inputRect)
            if enter=='ENTER'and len(username)>=1:
                username_take_time -= 1
        else:
            start_thread(recv_msg)
            connected =  True
    elif grid.game_over:  
        if res==None:
            header = 'GAME OVER!'
        elif res==player:
            header = 'YOU WIN'
        else:
            header = '{} WIN'.format(opponent)
        grid.write_text(surface, header, 235, 260, 50)
        grid.write_text(surface, 'Win : '+str(win), 240, 320, 30, (104,200,225))
        grid.write_text(surface, 'Lose : '+str(lose), 234, 350, 30, (104,200,225))
        grid.button(surface, 'RESTART', 165, 380, 140, 60, (0,200,0), (0,255,0))
    else:
        header = 'Your Turn' if turn==1 else "{}'s Turn".format(opponent)
        grid.write_text(surface, header, 235, 25, 25)      
        grid.draw_sign(surface)
        grid.draw_line(surface)        
        if grid.cnt==1:
            res = grid.check()
            if grid.game_over:
                if res is not None:
                    if res==player:
                        win += 1
                    else:
                        lose += 1
                    print(f'{opponent} win.')
                else:
                    print('Game over!')
                grid.update(surface, header, res)
                time.sleep(2)

    pygame.display.update()

    