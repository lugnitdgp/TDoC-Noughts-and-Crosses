import pygame
from grid import Grid
import os
import threading
import socket

os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'  #setting the relative position of the window

surface = pygame.display.set_mode((600,600)) # setting the grid size
pygame.display.set_caption('Tic-tac-toe')

def create_thread(target): # create a separate thread to send and receive data from the client
    thread = threading.Thread(target=target)
    thread.daemon = True # daemon thread does not block the main thread from exiting and continues to run in the background.
    thread.start()

# creating a TCP socket for the server

HOST = '127.0.0.1'  
PORT = 12345
connection_established = False
conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

def receive_data():
    global turn
    while True:
        data = conn.recv(1024).decode() # receive data from the client, it is a blocking method
        data = data.split('-') # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'O')

def waiting_for_connection():
    global connection_established, conn, addr
    conn, addr = sock.accept() # wait for a connection, it is a blocking method
    print(' Client is connected ! ')
    connection_established = True
    receive_data()


create_thread(waiting_for_connection) # run the blocking functions in a separate thread

grid = Grid() # creating a grid object
running = True
player = "X" # settting the marker
turn = True
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and connection_established:
            if pygame.mouse.get_pressed()[0]: # establishing the mouse button connection
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellX, cellY = pos[0] // 200, pos[1] // 200 # converting screen coordinates into cell coordinates
                    grid.get_mouse(cellX, cellY, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'yourturn', playing).encode()
                    conn.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False


    surface.fill((242,242,242))

    grid.draw(surface)

    pygame.display.flip()