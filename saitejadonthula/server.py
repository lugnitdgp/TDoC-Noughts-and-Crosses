
import socket
import threading
import pygame
from pygame.locals import *
import time


global k
inpt = 1
global l
global b
b=[0,8,1,7,2,6,3,5]

class Rnd(pygame.sprite.Sprite):
    def __init__(self, x , y):
        super(Rnd, self).__init__()
        self.surf =pygame.image.load("cir.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(x,y)
        )

class crs(pygame.sprite.Sprite):
    def __init__(self, x , y):
        super(crs, self).__init__()
        self.surf =pygame.image.load("crs.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(x,y)
        )
def nmbr(x,y):
    if 100 <= y < 300:
        if x<=200:
            return 0
        elif x<=400:
            return 1
        else:
            return 2
    elif 300 <= y < 500:
        if x<=200:
            return 3
        elif x<=400:
            return 4
        else:
            return 5
    else :
        if x<=200:
            return 6
        elif x<=400:
            return 7
        else:
            return 8



def chk():

  if l[4] != ' ':
       for i in range(0,8,2):
            if l[ b[i]]==l[4]:
                 if l[b[i+1]]==l[4]:
                      return  1
  if l[0] != ' ':

       if l[0]==l[1] and l[0]==l[2]:
            return 1
       elif l[0]==l[3] and l[0]==l[6]:
            return 1
  if l[8] != ' ':
       if l[8]==l[5] and l[8]==l[2]:
            return 1
       elif l[8]==l[7] and l[8]==l[6]:
            return 1
  else:
    return 0
def recv(s):
    print('waiting for msg')
    global inp
    global inpt
    for _ in range(5):

        inp = s.recv(1024).decode('utf-8')

        print(inp)
        if inp == 'quit':
            inpt = 2
            return
        else:
            inpt = 0


def thread_client(s):
    global inp
    global inpt
    global conn
    pygame.init()
    screen_wi = 600
    screen_hi = 700
    screen = pygame.display.set_mode((screen_wi, screen_hi))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill((0, 0, 0))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("other player's turn!", True, (255, 255, 255))
    poly = pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
    textRect = text.get_rect()
    textRect.center = (screen_wi // 2, 100 // 2)
    pygame.draw.line(screen, (0, 225, 0), (200, 120), (200, 680), 1)
    pygame.draw.line(screen, (0, 225, 0), (400, 120), (400, 680), 1)
    pygame.draw.line(screen, (0, 225, 0), (20, 300), (580, 300), 1)
    pygame.draw.line(screen, (0, 225, 0), (20, 500), (580, 500), 1)
    screen.blit(text, textRect)
    pygame.display.update()
    x = 1
    y = 1

    t = threading.Thread(target=recv,args=[conn,])
    t.daemon = True
    t.start()
    for i in range(5):
        while inpt ==1:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    conn.send(str.encode('quit'))
                    s.close()
                    return
            if inpt == 2:
                pygame.display.fill((0,100,0))
                text = font.render('connection lost !', True, (255, 255, 255), (0, 225, 0))
                screen.blit(text, textRect)
                pygame.display.flip()
                pygame.quit()
                s.close()
                return

        inpt ==1
        inp = int(inp)
        nw = Rnd((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)
        k.append(inp)
        l[inp] = "O"
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You lost the game ', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            s.close()
            b = 1
            break
        screen.blit(nw.surf, nw.rect)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        text = font.render('Select a Box !', True, (255, 255, 255), (0, 225, 0))
        screen.blit(text, textRect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    conn.send(str.encode('quit'))
                    s.close()
                    return
            if inpt == 2:
                screen.fill((0,100,0))
                text = font.render('connection lost !', True, (255, 255, 255), (0, 225, 0))
                screen.blit(text, textRect)
                pygame.display.flip()
                pygame.quit()
                s.close()
                return
            val = pygame.mouse.get_pressed()
            if val[0]:
                x, y = pygame.mouse.get_pos()

                inp = nmbr(x, y)
                if inp not in k:
                    break
        k.append(inp)
        conn.send(str.encode(str(inp)))
        nw = crs((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)
        l[inp] = "X"
        # pri()
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You won the game  !', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            # print('you won the game 🥳🥳🥳! ')
            s.close()
            b = 1
            break
        screen.blit(nw.surf, nw.rect)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        text = font.render("other player's turn!", True, (255, 255, 255), (0, 225, 0))
        screen.blit(text, textRect)
        pygame.display.update()
        inpt =1

    if b != 1:
        while inpt ==1:
            for event in pygame.event.get():
                if event.type == QUIT :
                    pygame.quit()
                    conn.send(str.encode('quit'))
                    s.close()
                    return
            if inpt == 2:
                pygame.fill((0,100,0))
                text = font.render('connection lost !', True, (255, 255, 255), (0, 225, 0))
                screen.blit(text, textRect)
                pygame.display.flip()
                pygame.quit()
                s.close()
                return
        inp = int(inp)
        inpt = 1
        l[inp] = "O"
        nw = Rnd((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)

        # pri()
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You lost the game!', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            # print('you won the game 🥳🥳🥳! ')
            s.close()
            b = 1

    if b != 1:
        screen.blit(nw.surf, nw.rect)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        text = font.render('Game is draw !', True, (255, 255, 255), (0, 225, 0))
        screen.blit(text, textRect)
        pygame.display.update()
        s.close()
    for _ in range(3):
        pygame.draw.polygon(screen, (225, 0, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        screen.blit(text, textRect)
        pygame.display.update()
        time.sleep(0.5)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        screen.blit(text, textRect)
        pygame.display.update()
        time.sleep(0.5)




def connfun(s):
    global conn
    global tr
    print('witing for connection..')
    conn,addr=s.accept()
    tr = 1



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 10000
s.bind((host, port))
s.listen(5)

tr = 0
pnt_lk = threading.Lock()
l =[i+1 for i in range(9)]

l = [' ']*9
k=[]
inpt = 1
inp = 1
conn = 0

t = threading.Thread(target=connfun,args=[s])
t.daemon = True
t.start()
while tr==0:
    pass
thread_client(s)
time.sleep(2)