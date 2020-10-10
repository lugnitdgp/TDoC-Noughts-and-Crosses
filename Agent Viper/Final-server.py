import socket
import sys
import pygame
from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN

)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

port = 1234
s.bind(('127.0.0.1', port))
print('Socket bound to port ' + str(port))

s.listen()
print('listening')

connection, address = s.accept()
print('Connected to ', address)
pygame.init()

white = [255, 255, 255]
line_colour = (0, 0, 0)
# pygame.display.set_caption('Tic Tac Toe')

# send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'yourturn', playing).encode() #sending data
#                     conn.send(send_data)
#  data = conn.recv(1024).decode() # receive data from the client, it is a blocking method
#         data = data.split('-') # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
img_x = pygame.image.load('X_modified.png')
img_o = pygame.image.load('o_modified.png')
img_x = pygame.transform.scale(img_x, (80, 80))
img_o = pygame.transform.scale(img_o, (80, 80))

screen = pygame.display.set_mode((500, 500))
screen.fill(white)

t = [['', '', ''], ['', '', ''], ['', '', '']]
running = True
c = 0
array = ['', '', '']


def game_initiating_window():
    # drawing vertical lines
    pygame.draw.line(screen, line_colour, (500 / 3, 0), (500 / 3, 500), 7)
    pygame.draw.line(screen, line_colour, (500 / 3 * 2, 0), (500 / 3 * 2, 500), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, line_colour, (0, 500 / 3), (500, 500 / 3), 7)
    pygame.draw.line(screen, line_colour, (0, 500 / 3 * 2), (500, 500 / 3 * 2), 7)
    # draw_status()

    pygame.display.update()
    

def draw(a):
    for i in range(3):
        for j in range(3):
            if int(a[0]) == i and int(a[1]) == j:
                if str(a[2]) == 'X':
                    screen.blit(img_x, ((2 * i + 1) * (500 / 6) + 30, (2 * j + 1) * (500 / 6) + 30))
                elif str(a[2]) == 'O':
                    screen.blit(img_o, ((2 * i + 1) * (500 / 6) + 30, (2 * j + 1) * (500 / 6) + 30))
    pygame.display.update()

    check_win(a)


def user_click():
    global array
    g, h = pygame.mouse.get_pos()
    if (g < 500 / 3):
        array[1] = 0
    elif (g < 2 * 500 / 3) and (g > 500 / 3):
        array[1] = 1
    elif (g < 500) and (g > 2 * 500 / 3):
        array[1] = 2
    if (h < 500 / 3):
        array[0] = 0
    elif (h < 2 * 500 / 3) and (h > 500 / 3):
        array[0] = 1
    elif (h < 500) and (h > 2 * 500 / 3):
        array[0] = 2

    if array[0] and array[1]:
        draw(array)


def check_win(b):
    global t
    for i in range(3):
        for j in range(3):
            if (not t[i][j]) and int(b[0]) == i and int(b[1]) == j:
                t[i][j] = b[2]

    g = 0
    if t[0][0] == t[0][1] and t[0][0] == t[0][2] and (t[0][0] == 'X' or t[0][0] == 'O'):
        g = 1
    elif t[1][0] == t[1][1] and t[1][0] == t[1][2] and (t[1][0] == 'X' or t[1][0] == 'O'):
        g = 1
    elif t[2][0] == t[2][1] and t[2][0] == t[2][2] and (t[2][0] == 'X' or t[2][0] == 'O'):
        g = 1
    elif t[0][1] == t[1][1] and t[0][1] == t[2][1] and (t[0][1] == 'X' or t[0][1] == 'O'):
        g = 1
    elif t[0][0] == t[1][0] and t[0][0] == t[2][0] and (t[0][0] == 'X' or t[0][0] == 'O'):
        g = 1
    elif t[0][2] == t[1][2] and t[0][2] == t[2][2] and (t[0][2] == 'X' or t[0][2] == 'O'):
        g = 1
    elif t[0][0] == t[1][1] and t[0][0] == t[2][2] and (t[0][0] == 'X' or t[0][0] == 'O'):
        g = 1
    elif t[0][2] == t[1][1] and t[0][2] == t[2][0] and (t[1][1] == 'X' or t[1][1] == 'O'):
        g = 1
    if c % 2 == 0 and g == 1:
        print('You win!')
        connection.close()
        s.close()
        sys.exit()
    elif c % 2 != 0 and g == 1:
        print('You lose!')
        connection.close()
        s.close()
        sys.exit()

game_initiating_window()

while running:

    if c % 2 != 0:
        data = connection.recv(1024).decode()
        data = data.split('-')
        # data=['x','y','X' or 'O']
        array[0] = data[0]
        array[1] = data[1]
        array[2] = data[2]
        draw(array)
    else:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                connection.close()
                s.close()
                sys.exit()
            if event.type is MOUSEBUTTONDOWN:
                print('4')
                user_click()
                send_data = '{}-{}-{}'.format(array[0], array[1], 'X').encode()  # sending data
                connection.send(send_data)

    c += 1
