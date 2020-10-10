import pygame, sys, _thread, socket, time
from pygame.locals import *
s = socket.socket()
s.bind(('', 12345))
s.listen()
pygame.init()
print("Listening")
c, addr = s.accept()
print("Connected to", addr)
DISPLAYSURF = pygame.display.set_mode((300, 400), 0, 32)
pygame.display.set_caption('Server')
WHITE = (255, 255, 255)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 100), (300, 100), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 200), (300, 200), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 300), (300, 300), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (100, 0), (100, 300), 1)
pygame.draw.line(DISPLAYSURF, WHITE, (200, 0), (200, 300), 1)
l1 = [[' ' for i in range(3)] for i in range(3)]
l2 = []


def check(player):
    flag = False
    for i in range(3):
        if l1[i][0] == l1[i][1] and l1[i][1] == l1[i][2] and l1[i][2] == l1[i][0] and (l1[i][0] == 'x' or l1[i][0] == 'o'):
            flag = True
            string = player + " wins!"
            pygame.draw.line(DISPLAYSURF, WHITE, (i * 100 + 50, 30), (i * 100 + 50, 270), 1)
            pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
            font = pygame.font.Font('freesansbold.ttf', 25)
            screen_text = font.render(string, True, WHITE)
            DISPLAYSURF.blit(screen_text, [10, 310])
            c.send(str.encode(player + " wins! " + str(i * 100 + 50) + ' 30 ' + str(i * 100 + 50) + ' 270'))
            break
        if l1[0][i] == l1[1][i] and l1[1][i] == l1[2][i] and l1[2][i] == l1[0][i] and (l1[0][i] == 'x' or l1[0][i] == 'o'):
            flag = True
            string = player + " wins!"
            pygame.draw.line(DISPLAYSURF, WHITE, (30, i * 100 + 50), (270, i * 100 + 50), 1)
            pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
            font = pygame.font.Font('freesansbold.ttf', 25)
            screen_text = font.render(string, True, WHITE)
            DISPLAYSURF.blit(screen_text, [10, 310])
            c.send(str.encode(player + " wins! " + '30 ' + str(i * 100 + 50) + ' 270 ' + str(i * 100 + 50)))
            break
    if l1[0][0] == l1[1][1] and l1[1][1] == l1[2][2] and l1[2][2] == l1[0][0] and (l1[0][0] == 'x' or l1[0][0] == 'o'):
        flag = True
        string = player + " wins!"
        pygame.draw.line(DISPLAYSURF, WHITE, (50, 50), (250, 250), 1)
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
        c.send(str.encode(player + " wins! 50 50 250 250"))
    if l1[0][2] == l1[1][1] and l1[1][1] == l1[2][0] and l1[2][0] == l1[0][2] and (l1[1][1] == 'x' or l1[1][1] == 'o'):
        flag = True
        string = player + " wins!"
        pygame.draw.line(DISPLAYSURF, WHITE, (250, 50), (50, 250), 1)
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
        c.send(str.encode(player + " wins! 250 50 50 250"))
    if ' ' not in [l1[0][0], l1[0][1], l1[0][2], l1[1][0], l1[1][1], l1[1][2], l1[2][0], l1[2][1], l1[2][2]] and flag != True:
        flag = True
        string = "Draw!"
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
        c.send(str.encode("Draw!"))
    if flag == False:
        string = "Server's move!"
        if player == "Server":
            string = "Client's move"
        c.send(str.encode(string))
        pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
        font = pygame.font.Font('freesansbold.ttf', 25)
        screen_text = font.render(string, True, WHITE)
        DISPLAYSURF.blit(screen_text, [10, 310])
    return flag


def gui():
    print("gui started")
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                c.send(str.encode("Server Gone!"))
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and my < 300 and str(mx // 100) + ' ' + str(my // 100) not in l2:
                x1 = 100 * (mx // 100) + 50
                y1 = 100 * (my // 100) + 50
                pygame.draw.line(DISPLAYSURF, WHITE, (x1 + 10, y1 + 10), (x1 - 10, y1 - 10), 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (x1 - 10, y1 + 10), (x1 + 10, y1 - 10), 2)
                c.send(str.encode(str(mx // 100) + ' ' + str(my // 100)))
                l2.append(str(mx // 100) + ' ' + str(my // 100))
                l1[mx // 100][my // 100] = 'x'
                t_f = check("Server")
                if t_f == True:
                    s.close()
        pygame.display.update()
    

def trial():
    print("trial started")
    t_f = False
    while t_f == False:
        string = str(c.recv(1024), "utf-8")
        try:
            i, j = string.split()
            l2.append(i + ' ' + j)
            l1[int(i)][int(j)] = 'o'
            pygame.draw.circle(DISPLAYSURF, WHITE, (100 * int(i) + 50, 100 * int(j) + 50), 15, 2)
            t_f = check("Client")
        except:
            pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 350), (300, 350), 100)
            font = pygame.font.Font('freesansbold.ttf', 32)
            screen_text = font.render(string, True, WHITE)
            DISPLAYSURF.blit(screen_text, [10, 310])
            break
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