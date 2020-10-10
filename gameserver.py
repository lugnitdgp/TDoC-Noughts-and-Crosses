import socket
import time
import pygame
from gamefunctions import *
import threading
import os
#os.environ['SDL_VIDEO_WINDOW_POS'] = '850,100'
os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'
#Color codes
black = 0, 0, 0
white=255,255,255
red = (255,0,0)
cyan=(0, 255, 255)
#***************
X,Y=600,600
fps = 30
surface=pygame.display.set_mode((X,Y+100),0,32)
pygame.display.set_caption("TIC-TAC-TOE PLAYER-1")
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (X,Y))
cover=pygame.image.load('cover.webp')
cover= pygame.transform.scale(cover, (X,Y))
#pygame.display.update()
CLOCK = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
text1= font.render('WELCOME :)',True,cyan,black)
textRect1= text1.get_rect()
textRect1.center = (300,625) 
text = font.render('CLICK TO START THE GAME', True,cyan,black) 
textRect = text.get_rect()
textRect.center = (300,675) 

#**********************************************************************************#
def new_thread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()
    
host=socket.gethostname()
port=9999
connection_established=False
conn,addr=None,None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
from_addr =(host,port)
s.bind(from_addr)
s.listen(1) #connection to the client(another player)

#******************************************************************************
def connecting():
    global connection_established,conn,addr
    conn,addr=s.accept()
    print("Another Player connected")
    connection_established=True
    receive_data()

def receive_data():
    global turn
    while True:
        #receive data from client
        data = conn.recv(1024).decode()
        # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        data = data.split('-') 
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn': #alter turns 
            turn = True
        if data[3] == 'False':
            grid.game_ended = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'O') #reset 
            grid.check_win(x, y, 'O')

#executing the function 
new_thread(connecting)

grid=Grid()
player="X"
playing='True'
turn =True
run=True

surface.blit(cover,(0, 0))
pygame.display.flip()
surface.blit(text1, textRect1)
pygame.display.flip()
surface.blit(text, textRect)
pygame.display.flip()

while run:
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            run = False
       if event.type == pygame.MOUSEBUTTONDOWN:
           surface.blit(background,(0, 0))
           pygame.display.flip()
           
       
       if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            
            if pygame.mouse.get_pressed()[0]:
                if not grid.game_ended and turn:
                    position=pygame.mouse.get_pos()
                    grid.get_mouse(position[0]//200,position[1]//200,player)
                    if grid.game_ended:
                        playing=False
                    send_data ='{}-{}-{}-{}'.format(position[0]//200, position[1]//200, 'yourturn', playing).encode() #sending data 
                    conn.send(send_data)
                    turn=False
                        
       if event.type == pygame.KEYDOWN:
    #after game is over it can be started again by pressing spacebar
            if event.key == pygame.K_SPACE and grid.game_ended:
                grid.reset_grid()
                grid.game_ended = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE: # starts a new game logic 
                run = False


    
    grid.draw(surface)
    pygame.display.flip()
    if run==False:
        pygame.quit()
                     


                    
        
    
    
    
