import sys
import socket
import pygame
from gamefunctions import *
import threading
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '850,100'
#Color codes
black = 0, 0, 0
white=255,255,255
red = (255,0,0)
cyan=(0, 255, 255)
#***************
X,Y=600,600
surface=pygame.display.set_mode((X,Y+100))
pygame.display.set_caption("TIC-TAC-TOE PLAYER-2")
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (X,Y))

font = pygame.font.Font('freesansbold.ttf', 32)
text1= font.render('WELCOME :)',True,red,black)
textRect1= text1.get_rect()
textRect1.center = (300,625)
text = font.render('CLICK TO START THE GAME', True,red,black)
textRect = text.get_rect()
textRect.center = (300,675)

#*********************************************************************************
host=socket.gethostname()
port=9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
from_addr =(host,port)
s.connect(from_addr)
#*********************************************************************************
def new_thread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()
def receive_data():
    global turn
    while True:
        #receive data from server
        data = s.recv(1024).decode()
        # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        data = data.split('-') 
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn': #alter turns 
            turn = True
        if data[3] == 'False':
            grid.game_ended = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'X') #reset 
            grid.check_win(x, y, 'X')

new_thread(receive_data)
player = "O"
grid = Grid()
playing ='True'
run= True
turn = False #client will wait for the server to make the first move
## Client ##
surface.blit(text1, textRect1)
pygame.display.flip()
surface.blit(text, textRect)
pygame.display.flip()



while run:
    surface.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_ended:
            if pygame.mouse.get_pressed()[0]:
                if not grid.game_ended and turn:
                    position=pygame.mouse.get_pos()
                    grid.get_mouse(position[0]//200,position[1]//200,player)
                    if grid.game_ended:
                        playing=False
                    send_data = '{}-{}-{}-{}'.format(position[0]//200,position[1]//200, 'yourturn', playing).encode() #sending data 
                    s.send(send_data)
                    turn=False
                        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_ended:
                grid.reset_grid()
                grid.game_ended = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE: # starts a new game logic 
                run = False


   
    grid.draw(surface)
    pygame.display.flip()
    
    
