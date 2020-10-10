import threading
import socket
import pygame
import numpy as np
conn = None
add = None
board = np.array([['','',''],['','',''],['','','']])
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ""
port = 10000
s.bind((host,port))
s.listen(10)

def recieve_data():
    a = True
    while a:
        da_ta = conn.recv(1024).decode()
        if da_ta == 'PLAYER ENDED GAME':
            update_text(screen,da_ta)
        else:
            x,y = da_ta.split(',')
            update_text(screen,"YOUR MOVE")
            a = draw_symbols(screen,x,y,'X')
    s.close()

    

def check_connection():
    global conn
    global add
    conn, add = s.accept()
    recieve_data()

def create_thread(fun):
    t = threading.Thread(target = fun)
    t.daemon = True
    t.start()

def get_pos(x,y):
    row = int(x/100)+1
    col = int(y/100)+1
    return(row,col)

def check_win():
    value = None
    a = 0
    k = (0,0)
    l = (0,0)
    for i in range(3):
        for j in range(3):
            if board[i][j]!='':
                a = a+1
    if board[0][0]==board[0][1] and board[0][0]==board[0][2] and board[0][0]!='':
        value = board[0][0]
        k = (0,50)
        l = (300,50)
    elif board[1][0]==board[1][1] and board[1][0]==board[1][2] and board[1][0]!='':
        value = board[1][0]
        k = (0,150)
        l = (300,150)
    elif board[2][0]==board[2][1] and board[2][0]==board[2][2] and board[2][0]!='':
        value = board[2][0]
        k = (0,250)
        l = (300,250)
    elif board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0]!='':
        value = board[0][0]
        k = (50,0)
        l = (50,300)
    elif board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1]!='':
        value = board[0][1]
        k = (150,0)
        l = (150,300)
    elif board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2]!='':
        value = board[0][2]
        k = (250,0)
        l = (250,300)
    elif board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!='':
        value = board[0][0]
        k = (0,0)
        l = (300,300)
    elif board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!='':
        value = board[0][2]
        k = (300,0)
        l = (0,300)
    elif a == 9:
        value = 'tie'
    return(value,k,l)

def draw_symbols(screen,x,y,thext):
    b = True
    board[int(y)-1][int(x)-1] = thext
    font = pygame.font.Font('freesansbold.ttf',50)
    text = font.render(thext, True, (255,255,0), (0,0,255))
    textRect=text.get_rect()
    textRect.center = (50+(100*(int(float(x))-1)),50+(100*(int(float(y))-1)))
    screen.blit(text, textRect)
    pygame.display.update()
    res,k,l = check_win()
    if res== 'X' or res == 'O' or res == 'tie':
        if res!= 'tie':
            update_text(screen,'PLAYER_'+res+' HAVE WON THE GAME')
            pygame.draw.line(screen, (255,127,80),k,l, 5)
            b = False
        else:
            update_text(screen,'MATCH HAS BEEN TIED')
            b = False
    return(b)
    
def update_text(screen,thext):
    pygame.draw.rect(screen, (0, 255, 0),(0,300,300,100))
    font = pygame.font.Font('freesansbold.ttf',17)
    text = font.render(thext, True, (255,20,147), (0,255,0))
    textRect=text.get_rect()
    textRect.center = (150,350)
    screen.blit(text, textRect)
    pygame.display.update()



pygame.init()
screen = pygame.display.set_mode([300, 400])
pygame.display.set_caption('TIC TAC TOE PLAYER2_O')
pygame.draw.rect(screen, (0, 0, 255),(0,0,300,300))
pygame.draw.rect(screen, (0, 255, 0),(0,300,300,100))
pygame.draw.line(screen, (0,255,0),(100,0),(100,300), 5)
pygame.draw.line(screen, (0,255,0),(200,0),(200,300), 5)
pygame.draw.line(screen, (0,255,0),(0,100),(300,100), 5)
pygame.draw.line(screen, (0,255,0),(0,200),(300,200), 5)

create_thread(check_connection)

running  = True
update_text(screen,'WAITING FOR OTHER MOVE')
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if conn!=None:
                conn.send(str.encode('PLAYER ENDED GAME'))
            running = False
        elif pygame.mouse.get_pressed() == (1,0,0):
            x, y = pygame.mouse.get_pos()
            x,y = get_pos(x,y)
            if conn!=None:
                tup = str(x)+','+str(y)
                conn.send(str.encode(tup))
            update_text(screen,'WAITING FOR OTHER MOVE')
            sai = draw_symbols(screen,x,y,"O")
            
            
            
            
    pygame.display.flip()


pygame.quit()
