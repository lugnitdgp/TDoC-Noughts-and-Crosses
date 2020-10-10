import pygame
from grid import Grid
import threading
import socket
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '700,100'

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

# create a separate thread to send and receive data from the server

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True  # daemon thread does not block the main thread from exiting and continues to run in the background.
    thread.start()

# creating a TCP socket for the client

HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def receive_data():
    global turn
    while True:
        data = sock.recv(1024).decode() # receive data from the server, it is a blocking method
        data = data.split('-') # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'X')

# run the blocking functions in a separate thread
create_thread(receive_data)

grid = Grid()
running = True
player = "O"
turn = False # client will wait for the server to make the first move
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellX, cellY = pos[0] // 200, pos[1] // 200
                    grid.get_mouse(cellX, cellY, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'yourturn', playing).encode()
                    sock.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((69,61,85))

    grid.draw(surface)

    pygame.display.flip()