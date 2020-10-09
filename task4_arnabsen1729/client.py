import socket
import pygame
import sys
import time
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
draw_textRect = draw_text.get_rect()
p1WinRect = p1Win.get_rect()
p2WinRect = p2Win.get_rect()
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
text1Rect.center = (WIDTH // 2, 25)
text2Rect.center = (WIDTH // 2, 25)
draw_textRect.center = (WIDTH // 2, HEIGHT//2)
p1WinRect.center = (WIDTH // 2, HEIGHT//2)
p2WinRect.center = (WIDTH // 2, HEIGHT//2)
pygame.display.set_caption('Player 2')
cross = pygame.image.load('img/cross.png')
circle = pygame.image.load('img/circle.png')


class Client:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        try:
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.DISCON_MSG = DISCON_MSG
            self.ADDR = ADDR
            self.SOCK.connect(ADDR)
            print(f'[NEW CONNECTION] Client {ADDR} added...')
        except:
            print('[SOMETHING WENT WRONG]...')
        

    def send_message(self, message, FORMAT='utf-8'):
        self.SOCK.sendall(bytes(str(message), FORMAT))
        if message == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        
    def recv_resp(self, CHUNKS=1024, FORMAT='utf-8'):
        data = self.SOCK.recv(CHUNKS).decode(FORMAT)
        # print(f'[RESPONSE FROM {self.ADDR}] : {data}')
        return int(data)





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

def mainGame(client):
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
            client.SOCK.close()
            sys.exit(0)
            break
        game_state = check_game_over(moves)
        if(game_state[0]):
            if who == 0:
                p1wins_draw(game_state[1], game_state[2])
            else:
                p2wins_draw(game_state[1], game_state[2])

            running = False
            client.SOCK.close()
            sys.exit(0)
            break

        display_grid()
        # pygame.draw.line(screen, (0, 0, 0), coord[0], coord[2], 3)
        if who==1:
            print('[WAITING FOR OPPONENT\'S MOVE...]')
            p1_index = client.recv_resp()
            print(f'[PLAYER 1 PLAYED]: {p1_index}')
            board[p1_index]=who
            who=0
            moves+=1
        else:
            # print('[WAITING FOR YOUR MOVE...]')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    client.SOCK.close()
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
                        print(f'[PLAYER 2 PLAYED]: {index}')
                        client.send_message(index)
                        moves += 1
                        who = 1
                        print(board, check_game_over(moves-1))
        display_board(moves)
        pygame.display.flip()
        pygame.display.update()


# mainGame()


HOST = socket.gethostname()
PORT = 3033 # change this to the port client1 is running
ADDR = (HOST, PORT)

p2 = Client(ADDR, 'Q')
print('[YOU ARE PLAYER 2]')
print('[GAME STARTED]')
mainGame(p2)
