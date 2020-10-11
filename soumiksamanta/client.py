#! /usr/bin/python3

import sys
import time
import socket
import pygame as pg

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
white = (246, 246, 246)
black = (37, 37, 38)
line_color = (22, 22, 22)
red = (250, 70, 70)
fps = 30

HOST = socket.gethostname() 
PORT = 9989
CLIENT = None
BUFF_SIZE = 1024

def create_client():
    global CLIENT
    try:
        CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print("Socket Creation Error!!\n", e)
        exit()

def connect_client():
    global CLIENT
    try:
        CLIENT.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Connection Error!!  Retrying...")
        time.sleep(2)
        connect_client()

def draw(row, col, player):
    if row == 1:
        posx = 30 + 40
    elif row == 2:
        posx = WINDOW_WIDTH/3 + 30 + 40
    elif row == 3:
        posx = WINDOW_WIDTH/3*2 + 30 + 40

    if col == 1:
        posy = 30
    elif col == 2:
        posy = WINDOW_HEIGHT/3 + 30
    elif col == 3:
        posy = WINDOW_HEIGHT/3*2 + 30

    if player == 'X':
        screen.blit(x_img, (posy, posx))
    elif player == 'O':
        screen.blit(o_img, (posy, posx))
    
    pg.display.update()


def checkWin(boardMatrix):
    res = None
    # check rows
    if boardMatrix[0][0] == boardMatrix[0][1] and boardMatrix[0][0] == boardMatrix[0][2] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, (0, (0+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), (WINDOW_WIDTH, (0+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), 4)
    if boardMatrix[1][0] == boardMatrix[1][1] and boardMatrix[1][0] == boardMatrix[1][2] and boardMatrix[1][0] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, (0, (1+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), (WINDOW_WIDTH, (1+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), 4)
    if boardMatrix[2][0] == boardMatrix[2][1] and boardMatrix[2][0] == boardMatrix[2][2] and boardMatrix[2][0] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, (0, (2+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), (WINDOW_WIDTH, (2+1)*WINDOW_HEIGHT/3 - WINDOW_HEIGHT/6 + 40), 4)

    # check columns
    if boardMatrix[0][0] == boardMatrix[1][0] and boardMatrix[0][0] == boardMatrix[2][0] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, ((0+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, 0 + 40), ((0+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, WINDOW_HEIGHT + 40), 4)
    if boardMatrix[0][1] == boardMatrix[1][1] and boardMatrix[0][1] == boardMatrix[2][1] and boardMatrix[0][1] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, ((1+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, 0 + 40), ((1+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, WINDOW_HEIGHT + 40), 4)
    if boardMatrix[0][2] == boardMatrix[1][2] and boardMatrix[0][2] == boardMatrix[2][2] and boardMatrix[0][2] != -1:
        res = boardMatrix[0][0]
        pg.draw.line(screen, red, ((2+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, 0 + 40), ((2+1)*WINDOW_WIDTH/3-WINDOW_WIDTH/6, WINDOW_HEIGHT + 40), 4)

    # check diagonals
    if boardMatrix[0][0] == boardMatrix[1][1] and boardMatrix[0][0] == boardMatrix[2][2] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
        pg.draw.line (screen, (250, 70, 70), (50, 50 + 40), (350, 350 + 40), 4)
    if boardMatrix[0][2] == boardMatrix[1][1] and boardMatrix[0][2] == boardMatrix[2][0] and boardMatrix[0][2] != -1:
        res = boardMatrix[0][0]
        pg.draw.line (screen, (250, 70, 70), (350, 50 + 40), (50, 350 + 40), 4)

    print(res)

    #checkDraw
    if res == None and not (any(-1 in row for row in boardMatrix)):
        return -1
    return res

def getClickIndex():
    x, y = pg.mouse.get_pos()

    if x < WINDOW_WIDTH/3:
        col = 0
    elif x < WINDOW_WIDTH/3*2:
        col = 1
    elif x < WINDOW_WIDTH:
        col = 2
    else:
        col = None
    
    if y < WINDOW_HEIGHT/3:
        row = 0
    elif y < WINDOW_HEIGHT/3*2:
        row = 1
    elif y < WINDOW_HEIGHT:
        row = 2
    else:
        row = None

    if row != None and col != None:
        return row, col
    return None, None

def communicate():
    global CLIENT, PORT
    CLIENT.send(bytes('CONNECT', 'utf-8'))
    
    player_msg = CLIENT.recv(BUFF_SIZE)
    player_msg = player_msg.decode('utf-8')
    if player_msg == 'QUIT':
        print('Lost connection with peer!! Quitting...')
        drawStatus('Lost connection with peer!! Quitting...')
        time.sleep(2)
        return
    print(player_msg)
    drawTop(player_msg)
    drawStatus(player_msg)

    player = player_msg[-1]

    boardMatrix = [[-1, -1, -1],
                   [-1, -1, -1],
                   [-1, -1, -1]]
    
    if player == 'X':
        drawStatus("Your Move")
        waiting_for_move = True
        while(waiting_for_move):
            for event in pg.event.get(): 
                if event.type == pg.QUIT: 
                    pg.quit() 
                    sys.exit() 
                elif event.type is pg.MOUSEBUTTONDOWN:
                    row, col = getClickIndex()
                    if row != None and col != None:
                        waiting_for_move = False
                        break
            pg.display.update() 
            CLOCK.tick(fps)
        self_move = str(row*3+col+1)
        boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 1

        CLIENT.send(bytes(self_move, 'utf-8'))
        draw(row+1, col+1, 'X')

    while True:
        drawStatus("Waiting for opponent's move...")
        peer_move = CLIENT.recv(BUFF_SIZE)
        
        # Check if connected
        if not peer_move:
            print('Disconnected from server!! Quitting...')
            drawStatus('Disconnected from server!! Quitting...')
            time.sleep(2)
            break
        peer_move = peer_move.decode('utf-8')
        
        # Check game over
        if peer_move == '[GAME OVER]':
            peer_move = CLIENT.recv(BUFF_SIZE)
            if player == 'X':
                boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 0
                draw((int(peer_move)-1)//3+1, (int(peer_move)-1)%3+1, 'O')
            else:# player == 'O':
                boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 1
                draw((int(peer_move)-1)//3+1, (int(peer_move)-1)%3+1, 'X')            
            print('[GAME OVER]')
            res = checkWin(boardMatrix)
            if res == -1:
                print('----DRAW----')
                drawStatus("DRAW")
                time.sleep(2)
                CLIENT.close()
                if drawPlayAgain():
                    create_client()
                    connect_client()
                    initiate_game()
                    communicate()
                break
            print('Oops!! You Lost!!')
            drawStatus('Oops!! You Lost!!')
            time.sleep(2)
            CLIENT.close()
            if drawPlayAgain():
                create_client()
                connect_client()
                initiate_game()
                communicate()
            break
        elif peer_move == 'QUIT':
            drawStatus('Lost connection with peer!! Quitting...')
            time.sleep(2)
            break

        if player == 'X':
            boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 0
            draw((int(peer_move)-1)//3+1, (int(peer_move)-1)%3 +1, 'O')
        else:
            boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 1
            draw((int(peer_move)-1)//3+1, (int(peer_move)-1)%3 +1, 'X')
        

        drawStatus("Your Move")
        waiting_for_move = True
        while(waiting_for_move):
            for event in pg.event.get(): 
                if event.type == pg.QUIT: 
                    pg.quit() 
                    sys.exit() 
                elif event.type is pg.MOUSEBUTTONDOWN: 
                    row, col = getClickIndex()
                    if row != None and col != None and boardMatrix[row][col] == -1:
                        waiting_for_move = False
                        break
            pg.display.update() 
            CLOCK.tick(fps)
        self_move = str(row*3+col+1)

        if player == 'X':
            boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 1
            draw((int(self_move)-1)//3+1, (int(self_move)-1)%3+1, 'X')
        else:
            boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 0
            draw((int(self_move)-1)//3+1, (int(self_move)-1)%3+1, 'O')
        
        res = checkWin(boardMatrix)

        if res == None:
            CLIENT.send(bytes(self_move, 'utf-8'))
        elif res == -1:
            CLIENT.send(bytes('[GAME OVER]', 'utf-8'))
            print('[GAME OVER]')
            print('----DRAW----')
            time.sleep(0.5)
            CLIENT.send(bytes(self_move, 'utf-8'))
            drawStatus("DRAW")
            time.sleep(2)
            CLIENT.close()
            if drawPlayAgain():
                create_client()
                connect_client()
                initiate_game()
                communicate()
            break
        else:
            CLIENT.send(bytes('[GAME OVER]', 'utf-8'))
            print('[GAME OVER]')
            print('Congrats!! You Win!!')
            drawStatus('Congrats!! You Win!!')
            time.sleep(2)
            CLIENT.send(bytes(self_move, 'utf-8'))
            CLIENT.close()
            if drawPlayAgain():
                create_client()
                connect_client()
                initiate_game()
                communicate()
            break

def initiate_game():
    screen.blit(initiating_window, (0,0))

    pg.display.update()
    time.sleep(2)
    screen.fill(white)

    # vertical lines
    pg.draw.line(screen, line_color, (WINDOW_WIDTH/3, 40), (WINDOW_WIDTH/3, WINDOW_HEIGHT+40), 7)
    pg.draw.line(screen, line_color, (WINDOW_WIDTH/3*2, 40), (WINDOW_WIDTH/3*2, WINDOW_HEIGHT+40), 7)
    # horizontal lines
    pg.draw.line(screen, line_color, (0, WINDOW_WIDTH/3+40), (WINDOW_WIDTH, WINDOW_HEIGHT/3+40), 7)
    pg.draw.line(screen, line_color, (0, WINDOW_WIDTH/3*2+40), (WINDOW_WIDTH, WINDOW_HEIGHT/3*2+40), 7)
    
    drawTop("Welcome aboard")
    drawStatus("Waiting for an opponent...")
    pg.display.update()

def drawStatus(message):
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)
    screen.fill(black, (0, 440, 540, 100))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, 540-50))
    screen.blit(text, text_rect)
    pg.display.update()

def drawTop(message):
    font = pg.font.Font(None, 25)
    text = font.render(message, 1, white)
    screen.fill(black, (0, 0, 500, 40))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, 20))
    screen.blit(text, text_rect)
    pg.display.update()

def drawPlayAgain():
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)

    font = pg.font.SysFont('Corbel', 25)
    text = font.render("Play Again", 1, white)

    playAgain = False

    waiting = True
    while waiting:
        screen.fill(black)
        cursor_pos = pg.mouse.get_pos()

        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                pg.quit() 
                sys.exit() 
            elif event.type is pg.MOUSEBUTTONDOWN:                
                if WINDOW_WIDTH/2-100 <= cursor_pos[0] <= WINDOW_WIDTH/2+100 and (WINDOW_HEIGHT+140)/2-25 <= cursor_pos[1] <= (WINDOW_HEIGHT+140)/2+25:
                    playAgain = True
                    waiting = False
                    break
        if WINDOW_WIDTH/2-100 <= cursor_pos[0] <= WINDOW_WIDTH/2+100 and (WINDOW_HEIGHT+140)/2-25 <= cursor_pos[1] <= (WINDOW_HEIGHT+140)/2+25:
            pg.draw.rect(screen, color_light, [WINDOW_WIDTH/2-100, (WINDOW_HEIGHT+140)/2-25, 200, 50])
        else:
            pg.draw.rect(screen, color_dark, [WINDOW_WIDTH/2-100, (WINDOW_HEIGHT+140)/2-25, 200, 50])

        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, (WINDOW_HEIGHT+140)/2))
        screen.blit(text, text_rect)

        pg.display.update() 
        CLOCK.tick(fps)

    return playAgain

if __name__ == '__main__':
    create_client()
    connect_client()
    pg.init()
    
    CLOCK = pg.time.Clock()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + 100 + 40), 0, fps)
    pg.display.set_caption("Tic-Tac-Toe") 

    initiating_window = pg.image.load("cover.png") 
    symbol_x = pg.image.load("X.png") 
    symbol_o = pg.image.load("O.png")

    initiating_window = pg.transform.scale(initiating_window, (WINDOW_WIDTH, WINDOW_HEIGHT + 140)) 
    x_img = pg.transform.scale(symbol_x, (80, 80)) 
    o_img = pg.transform.scale(symbol_o, (80, 80)) 

    initiate_game()

    communicate()
    # CLIENT.close()
    pg.quit() 
    sys.exit()
    
