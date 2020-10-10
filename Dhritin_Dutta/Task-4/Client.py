import pygame, sys, _thread, socket, time
from pygame.locals import *
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected")
pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 400), 0, 32)
pygame.display.set_caption('Client')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 100), (300, 100), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 200), (300, 200), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 300), (300, 300), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (100, 0), (100, 300), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (200, 0), (200, 300), 1)
pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
font = pygame.font.Font("freesansbold.ttf", 32)
screen_text = font.render('Start!', True, WHITE)
DISPLAYSURF.blit(screen_text, [10, 310])
l2 = []


def gui():
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                s.send(str.encode("Client Gone!"))
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN and my < 300 and str(mx // 100) + ' ' + str(my // 100) not in l2:
            pygame.draw.circle(DISPLAYSURF, WHITE, (100 * (mx // 100) + 50, 100 * (my // 100) + 50), 15, 2)
            s.send(str.encode(str(mx // 100) + ' ' + str(my // 100)))
            l2.append(str(mx // 100) + ' ' + str(my // 100))
        pygame.display.update()
        
        
def trial():
    while True:
        string1 = str(s.recv(1024), "utf-8")
        string = string1
        if "wins" in string1:
            a, b, c, d, e, f = string1.split()
            string = a + ' ' + b
            pygame.draw.line(DISPLAYSURF, WHITE, (int(c), int(d)), (int(e), int(f)), 1)
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
        string2 = str(s.recv(1024), "utf-8")
        try:
            i, j = string2.split()
            print(i, j)
            x1 = 100 * int(i) + 50
            y1 = 100 * int(j) + 50
            pygame.draw.line(DISPLAYSURF, WHITE, (x1 + 10, y1 + 10), (x1 - 10, y1 - 10), 2)
            pygame.draw.line(DISPLAYSURF, WHITE, (x1 - 10, y1 + 10), (x1 + 10, y1 - 10), 2)
            l2.append(i + ' ' + j)
        except:
            pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
            font = pygame.font.Font("freesansbold.ttf", 32)
            screen_text = font.render(string2, True, WHITE)
            DISPLAYSURF.blit(screen_text, [10, 310])
            break
        string1 = str(s.recv(1024), "utf-8")
        string = string1
        if "wins" in string1:
            a, b, c, d, e, f = string1.split()
            string = a + ' ' + b
            pygame.draw.line(DISPLAYSURF, WHITE, (int(c), int(d)), (int(e), int(f)), 1)
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
    time.sleep(3)
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (150, 0), (150, 400), 300)
    font = pygame.font.Font('freesansbold.ttf', 25)
    screen_text = font.render("CLOSING...", True, WHITE)
    DISPLAYSURF.blit(screen_text, [80, 190])
    time.sleep(1)
    s.close()
    pygame.quit()
    sys.exit()
    
    
_thread.start_new_thread(trial, ())
gui()