
import socket
import threading
import pygame
from pygame.locals import *
import time


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


def recv(s):
    global inp
    global inpt
    for _ in range(4):
        inp = s.recv(1024).decode('utf-8')
        if inp == 'quit':
            inpt = 2
            return
        else:
            inpt =0


def thread_client(s):
    global inp
    global inpt
    conn = s
    pygame.init()
    screen_wi = 600
    screen_hi = 700
    screen = pygame.display.set_mode((screen_wi, screen_hi))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill((0, 0, 0))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Select a box !', True, (255, 255, 255))
    poly = pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
    textRect = text.get_rect()
    textRect.center = (screen_wi // 2, 100 // 2)
    pygame.draw.line(screen, (0, 225, 0), (200, 120), (200, 680), 1)
    pygame.draw.line(screen, (0, 225, 0), (400, 120), (400, 680), 1)
    pygame.draw.line(screen, (0, 225, 0), (20, 300), (580, 300), 1)
    pygame.draw.line(screen, (0, 225, 0), (20, 500), (580, 500), 1)
    screen.blit(text, textRect)
    pygame.display.update()

    inpt = 1
    t = threading.Thread(target=recv, args=[s, ])
    t.daemon = True
    t.start()
    x = 1
    y = 1
    g = 0
    for i in range(4):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            if inpt == 2:
                pygame.fill((0,100,0))
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
        l[inp] = "O"
        nw = Rnd((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)
        # all_photos.add(nw)
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You won the game !', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            # print('you won the game 🥳🥳🥳! ')
            s.close()
            g = 1
            break
        screen.blit(nw.surf, nw.rect)
        text = font.render("other player's turn!", True, (255, 255, 255), (0, 225, 0))
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        screen.blit(text, textRect)
        pygame.display.update()
        while inpt == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    s.send(str.encode('quit'))
                    s.close()
                    return
            if inpt == 2:
                screen.fill((0, 100, 0))
                text = font.render('connection lost !', True, (255, 255, 255), (0, 225, 0))
                screen.blit(text, textRect)
                pygame.display.flip()
                pygame.quit()
                s.close()
                return
        inp = int(inp)
        inpt = 1
        nw = crs((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)
        k.append(inp)
        l[inp] = "X"
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You lost the game !', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            s.close()
            g = 1
            break

        screen.blit(nw.surf, nw.rect)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
        text = font.render('Select a Box !', True, (255, 255, 255), (0, 225, 0))
        screen.blit(text, textRect)
        pygame.display.update()

    if g != 1:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            val = pygame.mouse.get_pressed()
            if inpt == 2:
                screen.fill((0,100,0))
                text = font.render('connection lost !', True, (255, 255, 255), (0, 225, 0))
                screen.blit(text, textRect)
                pygame.display.flip()
                pygame.quit()
                s.close()
                return
            if val[0]:
                x, y = pygame.mouse.get_pos()

                inp = nmbr(x, y)
                if inp not in k:
                    break
        k.append(inp)
        conn.send(str.encode(str(inp)))
        l[inp] = "O"
        nw = Rnd((inp % 3) * 200 + 100, int(inp / 3) * 200 + 200)
        # all_photos.add(nw)
        if chk():
            print(l)
            screen.blit(nw.surf, nw.rect)
            pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
            text = font.render('You won!', True, (255, 255, 255), (0, 225, 0))
            screen.blit(text, textRect)
            pygame.display.update()
            s.close()
            g = 1

    if g != 1:
        screen.blit(nw.surf, nw.rect)
        text = font.render('Game is draw !', True, (255, 255, 255), (0, 225, 0))
        screen.blit(text, textRect)
        pygame.draw.polygon(screen, (0, 225, 0), ((0, 0), (600, 0), (600, 100), (0, 100)))
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





def connfun():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(),10000))
    thread_client(s)


global l
global g
g=[0,8,1,7,2,6,3,5]

def chk():
  if l[4] != ' ':
       for i in range(0,8,2):
            if l[g[i]]==l[4]:
                 if l[g[i+1]]==l[4]:
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


b=0
l =[i+1 for i in range(9)]
l = [' ']*9
k =[]
connfun()
inp = 1
inpt = 1
time.sleep(2)