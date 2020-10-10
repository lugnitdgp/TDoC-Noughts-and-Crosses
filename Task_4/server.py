import pygame
import sys
import time
from pygame.locals import *
import socket
import threading
import os

# Poitioning The opening Window
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '350,100'

# for storing the 'x' or 'o' variables as characters and it denotes the respective moves 
XO = 'x'

# helps to check for the winner
winner = None

# to check if the game is a draw
draw = None

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# Background - Color
white = (255, 255, 255)

# color of the straightlines on the Dividing Board
line_color = (0, 0, 0)

# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]


# initializing the pygame window
pygame.init()

# setting fps manually
fps = 60

# this is used to track time
CLOCK = pygame.time.Clock()

# this method is used to build the infrastructure of the display
# added extra 150 for displaying the draw status and showing the player status
screen = pygame.display.set_mode((width, height + 150), 0, 32)

# setting up a nametag for the game tab
pygame.display.set_caption("Server")

# loading the images as python object
cover_img = pygame.image.load(os.path.join('images', 'cover.png'))
x_img = pygame.image.load(os.path.join('images', 'tic-tac-toe-x.png'))
y_img = pygame.image.load(os.path.join('images', 'tic-tactoe-o.png'))

# resizing image
cover_img = pygame.transform.scale(cover_img, (width, height + 100))
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(y_img, (80, 80))

# Defining A count Var
count = 0

conn_established = False

# create a separate thread to send and receive data from the client Since It is a blocking parameter

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

# Defining A connection Object
s = socket.socket()
#binding Host And Port
s.bind(('', 9999))
# Listening For Connection
s.listen(1)
# Accepting The Connection
conn, addr = s.accept()  # wait for a connection, it is a blocking method
conn_established = True
print('You Are Connected To ---- IP : ' + str(addr[0]) + ' port : ' + str(addr[1]))


# Function For Recieving data
def receive_data():
    global winner, draw, XO, conn
    while True:
        if XO == 'o':
            # get coordinates of mouse click
            data = conn.recv(1024).decode()
            if(data == 'quit'):
                conn = None
                exit()
                pygame.quit()
                sys.exit()
            data = data.split('-')
            x, y = int(data[0]), int(data[1])
            user_click(x, y)
            if(winner or draw):
                reset_game()
            pygame.display.update()
            CLOCK.tick(fps)


# run the blocking functions in a separate thread
create_thread(receive_data)


def game_initiating_window():
    screen.blit(cover_img, (0, 0)) 
      
    # updating the display 
    pygame.display.update() 
    time.sleep(3)                     
    screen.fill(white)
    # drawing vertical lines
    pygame.draw.line(screen, line_color, (width // 3, 0), (width // 3, height), 7)
    pygame.draw.line(screen, line_color, (width // 3 * 2, 0),
                 (width // 3 * 2, height), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, height // 3), (width, height // 3), 7)
    pygame.draw.line(screen, line_color, (0, height // 3 * 2),
                 (width, height // 3 * 2), 7)
    draw_status()


def draw_status():

    # getting the global variable draw into action
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    # setting a font object
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 20)

    # setting the font properties like
    # color and width of the text
    text = font.render(message, 1, (255, 255, 255))
    text1 = font1.render("You Are X", 1, (255, 255, 255))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 550, 150))
    text_rect = text.get_rect(center=(width // 2, 500-50))
    text_rect1 = text1.get_rect(center=(width // 2, 550-25))
    screen.blit(text, text_rect)
    screen.blit(text1 , text_rect1)
    pygame.display.update()

    # text1 Is the message that displays what player you are and the other shows Who will play now


def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(screen, (255, 233, 145),
                         (0, (row + 1)*height // 3 - height // 6),
                         (width, (row + 1)*height // 3 - height // 6),
                         4)
            break

    # checking for winning columns
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(screen, (255, 255, 255), ((col + 1) * width // 3 - width // 6, 0),
                         ((col + 1) * width // 3 - width // 6, height), 10)
            break

    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        # game won diagonally left to right
        winner = board[0][0]
        pygame.draw.line(screen, (255, 255, 255), (50, 50), (350, 350), 10)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

        # game won diagonally right to left
        winner = board[0][2]
        pygame.draw.line(screen, (255, 255, 255), (350, 50), (50, 350), 10)

    if(all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()


def drawXO(row, col):
    global board, XO

    # for the first row, the image
    # should be pasted at a x coordinate
    # of 30 from the left margin
    if row == 1:
        posx = 30

    # for the second row, the image
    # should be pasted at a x coordinate
    # of 30 from the game line
    if row == 2:

        # margin or width // 3 + 30 from
        # the left margin of the window
        posx = width // 3 + 30

    if row == 3:
        posx = width // 3 * 2 + 30

    if col == 1:
        posy = 30

    if col == 2:
        posy = height // 3 + 30

    if col == 3:
        posy = height // 3 * 2 + 30

    # setting up the required board
    # value to display
    board[row-1][col-1] = XO

    if(XO == 'x'):

        # pasting x_img over the screen
        # at a coordinate position of
        # (pos_y, posx) defined in the
        # above code
        screen.blit(x_img, (posy, posx))
        XO = 'o'

    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pygame.display.update()


def user_click(x, y):

    # get column of mouse click (1-3)
    if(x < width // 3):
        col = 1

    elif (x < width // 3 * 2):
        col = 2

    elif(x < width):
        col = 3

    else:
        col = None

    # get row of mouse click (1-3)
    if(y < height // 3):
        row = 1

    elif (y < height // 3 * 2):
        row = 2

    elif(y < height):
        row = 3

    else:
        row = None

    # after getting the row and col,
    # we need to draw the images at
    # the desired positions
    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row, col)
        check_win()

# Setting The Reset Window Such That The oppposite player can play
def reset_game():
    global board, winner, XO, draw , count
    time.sleep(3)
    draw = False
    if(count%2==0):
        XO = 'x'
    else:
        XO = 'o'
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

# Inintiating The Main Game Window
game_initiating_window()

while True:
    if(conn == None):
        pygame.quit()
        sys.exit()
    if(XO == 'x'):
        for event in pygame.event.get():
            if event.type == QUIT:
                conn.send('quit'.encode())
                pygame.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                # get coordinates of mouse click
                x, y = pygame.mouse.get_pos()
                user_click(x, y)
                send_data = '{}-{}'.format(x, y).encode()  # sending data
                conn.send(send_data)
                if(winner or draw):
                    count += 1
                    reset_game()
        pygame.display.update()
    CLOCK.tick(fps)

