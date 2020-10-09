import socket
import sys
# from gameLogic import TicTacToe
import pygame
import sys
import time
# from gameLogic import TicTacToe

pygame.init()
HEIGHT = 500
WIDTH = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('CaviarDreams.ttf', 32)
s1 = 'Player1\'s Move'
s2 = 'Player2\'s Move'
text1 = font.render(s1, True, (0, 0, 0))
text2 = font.render(s2, True, (0, 0, 0))
draw_text = font.render('Draw Match!', True, (0, 0, 0))
p1Win = font.render('Player1 Wins!', True, (0, 0, 0))
p2Win = font.render('Player1 Wins!', True, (0, 0, 0))
wait_for_opp = font.render('WAIT FOR YOU OPPONENT..', True, (0, 0, 0))
draw_textRect = draw_text.get_rect()
p1WinRect = p1Win.get_rect()
p2WinRect = p2Win.get_rect()
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
wait_for_oppRect = wait_for_opp.get_rect()
text1Rect.center = (WIDTH // 2, 25)
text2Rect.center = (WIDTH // 2, 25)
draw_textRect.center = (WIDTH // 2, HEIGHT//2)
p1WinRect.center = (WIDTH // 2, HEIGHT//2)
p2WinRect.center = (WIDTH // 2, HEIGHT//2)
wait_for_oppRect.center = (WIDTH // 2, HEIGHT//2)
pygame.display.set_caption('Player 1')
cross = pygame.image.load('img/cross.png')
circle = pygame.image.load('img/circle.png')


class Server:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        self.ADDR = ADDR
        self.DISCON_MSG = DISCON_MSG
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        self.SOCK.bind(self.ADDR)
        self.SOCK.listen()
        return self.SOCK

    def accept_client(self):
        conn, addr = self.SOCK.accept()
        print(f'[NEW CONNECTION] Client {addr} added...')
        return conn, addr

    def recv_message(self, conn, CHUNKS=1024, FORMAT='utf-8'):
        data = conn.recv(CHUNKS).decode(FORMAT)
        # print(f'[MESSAGE FROM {addr}] : {data}')
        if data == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        return int(data)
        
    def send_resp(self, conn, RESPONSE, FORMAT='utf-8'):
        conn.send(bytes(str(RESPONSE), FORMAT))


def getIndex(x, y):
    if 0 < x < 149:
        if 50 < y < 199:
            return 0
        if 201 < y < 349:
            return 3
        if 351 < y < 500:
            return 6
        else:
            return -1
    elif 151 < x < 299:
        if 50 < y < 199:
            return 1
        if 201 < y < 349:
            return 4
        if 351 < y < 500:
            return 7
        else:
            return -1
    elif 301 < x < 450:
        if 50 < y < 199:
            return 2
        if 201 < y < 349:
            return 5
        if 351 < y < 500:
            return 8
        else:
            return -1
    else:
        return -1


board = [-1] * 9  # initialising the board with -1, which means no moves

# dictionary of index and render coordinate
coord = {0: (50, 100),
         1: (200, 100),
         2: (350, 100),
         3: (50, 250),
         4: (200, 250),
         5: (350, 250),
         6: (50, 400),
         7: (200, 400),
         8: (350, 400)}

final_line = {0: (77, 127),
         1: (227, 127),
         2: (410, 127),
         3: (77, 277),
         4: (227, 277),
         5: (410, 277),
         6: (77, 427),
         7: (227, 427),
         8: (410, 427)}

# function to display cross and circle according to click coordinates and chance
def fade(): 
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.fill((255, 253, 208))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(3)


def display_sign(ind, sign):
    if ind != -1:
        if sign == 0:
            screen.blit(circle, coord[ind])
        if sign == 1:
            screen.blit(cross, coord[ind])


running = True
who = 1  # check if player will draw cross or circle
moves = 0  # total number of moves so far


def display_board(moves):
    if moves < 9 and moves % 2 == 0:
        screen.blit(text1, text1Rect)
    elif moves < 9:
        screen.blit(text2, text2Rect)

    for val in range(9):
        if board[val] == 1:
            display_sign(val, 1)
        elif board[val] == 0:
            display_sign(val, 0)


def check_game_over(moves):
    if moves < 5:
        return [False]
    elif board[0] == board[1] == board[2] and board[0] != -1:
        return [True, 0, 2]
    elif board[3] == board[4] == board[5] and board[3] != -1:
        return [True, 3, 5]
    elif board[6] == board[7] == board[8] and board[6] != -1:
        return [True, 6, 8]
    elif board[0] == board[3] == board[6] and board[0] != -1:
        return [True, 0, 6]
    elif board[1] == board[4] == board[7] and board[1] != -1:
        return [True, 1, 7]
    elif board[2] == board[5] == board[8] and board[2] != -1:
        return [True, 2, 8]
    elif board[0] == board[4] == board[8] and board[0] != -1:
        return [True, 0, 8]
    elif board[2] == board[4] == board[6] and board[2] != -1:
        return [True, 2, 6]
    else:
        return [False]




def game_draw():
    fade()
    screen.fill((255, 253, 208))
    print('[GAME DRAW]')
    screen.blit(draw_text, draw_textRect)
    pygame.display.flip()
    pygame.display.update
    time.sleep(2)


def p1wins_draw(l, r):
    global moves
    print('[PLAYER 1 WINS]')
    display_grid()
    display_board(moves)
    if ((l==0 and r==8) or (l==2 and r==6)):
        pygame.draw.line(screen, (0, 0, 0), coord[l], coord[r], 5)
    else:
        pygame.draw.line(screen, (0, 0, 0), final_line[l], final_line[r], 5)
    pygame.display.flip()
    pygame.display.update
    time.sleep(1)
    fade()
    moves = 9
    screen.fill((255, 253, 208))
    screen.blit(p1Win, p1WinRect)
    pygame.display.flip()
    pygame.display.update
    time.sleep(2)


def p2wins_draw(l, r):
    global moves
    print('[PLAYER 2 WINS]')
    display_grid()
    display_board(moves)
    if ((l==0 and r==8) or (l==2 and r==6)):
        pygame.draw.line(screen, (0, 0, 0), coord[l], coord[r], 5)
    else:
        pygame.draw.line(screen, (0, 0, 0), final_line[l], final_line[r], 5)
    pygame.display.flip()
    pygame.display.update
    time.sleep(1)
    fade()
    moves = 9
    screen.fill((255, 253, 208))
    screen.blit(p1Win, p1WinRect)
    pygame.display.flip()
    pygame.display.update
    time.sleep(2)

def display_grid():
    pygame.draw.line(screen, (255, 255, 255), (0, 50), (500, 50))
    pygame.draw.line(screen, (0, 0, 0), (20, 200), (430, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (20, 350), (430, 350), 2)
    pygame.draw.line(screen, (0, 0, 0), (20, 500), (430, 500), 2)

    pygame.draw.line(screen, (0, 0, 0), (150, 50), (150, 480), 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 50), (300, 480), 2)
    pygame.draw.line(screen, (0, 0, 0), (450, 50), (450, 480), 2)

def mainGame(conn, serv):
    # game = TicTacToe()

    global running
    global who
    global moves
    screen.fill((255, 253, 208))
    display_grid()
    display_board(moves)
    pygame.display.flip()
    pygame.display.update()
    while running:
        screen.fill((255, 253, 208))
        if(moves == 9):
            game_draw()
            running = False
            serv.SOCK.close()
            sys.exit(0)
            break
        game_state = check_game_over(moves)
        if(game_state[0]):
            if who == 0:
                p1wins_draw(game_state[1], game_state[2])
            else:
                p2wins_draw(game_state[1], game_state[2])

            running = False
            serv.SOCK.close()
            sys.exit(0)
            break

        display_grid()
        # pygame.draw.line(screen, (0, 0, 0), coord[0], coord[2], 3)
        if who == 0:
            print('[WAITING FOR OPPONENT\'S MOVE...]')
            p2_index = serv.recv_message(conn)
            print(f'[PLAYER 2 PLAYED]: {p2_index}')
            board[p2_index]=who
            who=1
            moves+=1
        else:
            # print('[WAITING FOR YOUR MOVE...]')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    serv.SOCK.close()
                    sys.exit(0)
                    return
                # or MOUSEBUTTONDOWN depending on what you want.
                if event.type == pygame.MOUSEBUTTONUP:
                    click_coord = event.pos

                    click_x = click_coord[0]
                    click_y = click_coord[1]
                    index = getIndex(click_x, click_y)
                    
                    if(board[index] == -1):
                        board[index] = who
                        print(f'[PLAYER 1 PLAYED]: {index}')
                        serv.send_resp(conn, index)
                        moves += 1
                        who = 0
        display_board(moves)
        pygame.display.flip()
        pygame.display.update()


# mainGame()


HOST = socket.gethostname()
PORT = 3033 # change this to any other available port
ADDR = (HOST, PORT)

p1 = Server(ADDR, 'Q')
server_sock = p1.init()
print('[YOU ARE PLAYER 1]')
print('Waiting for opponent...')
screen.fill((255, 253, 208))
screen.blit(wait_for_opp, wait_for_oppRect)
pygame.display.flip()
pygame.display.update
while server_sock:
    conn, addr = p1.accept_client()
    print('[GAME STARTED]')
    while True:
        mainGame(conn, p1)
