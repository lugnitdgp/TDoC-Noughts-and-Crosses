import socket
import threading
from pygame.locals import (K_ESCAPE, K_SPACE, KEYDOWN, MOUSEBUTTONUP, QUIT)
from tic_tac_toe import *


def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


host = '127.0.0.1'
port = 9876
conn, addr = None, None
connection_established = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)


def receive_data():
    while True:
        global turn
        data = conn.recv(1024).decode('utf-8')
        data = data.split(' ')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'your_turn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'O')


def waiting_for_connection():
    global connection_established, conn, addr
    conn, addr = s.accept()
    connection_established = True
    print('Client connected.')
    receive_data()


create_thread(waiting_for_connection)


# Creates the base screen/window.
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 540
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     # creates the main window with specific size.
pygame.display.set_caption('Tic Tac Toe')                           # set the window caption as 'Tic Tac Toe'
screen.fill((247, 231, 189))                                        # fills the window with specific colour.

grid = Grid()

player = "X"
turn = True
playing = 'True'

running = True
while running:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP and connection_established:
            if turn and not grid.game_over:
                position = pygame.mouse.get_pos()
                cell_x, cell_y = (position[0] // 150, position[1] // 180)
                grid.get_mouse(cell_x, cell_y, player)

                if grid.game_over:
                    playing = 'False'

                send_data = f'{cell_x} {cell_y} your_turn {playing}'.encode('utf-8')
                conn.send(send_data)
                turn = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            elif event.key == K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'

        elif event.type == QUIT:
            running = False

        screen.fill((247, 231, 189))
        grid.draw(screen)
        pygame.display.flip()

pygame.quit()

