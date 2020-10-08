#! /usr/bin/python3

import time
import socket

HOST = socket.gethostname() 
PORT = 9989
CLIENT = None
BUFF_SIZE = 1024

def create_client():
    global CLIENT
    try:
        CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CLIENT.connect((HOST, PORT))
    except:
        print("Connection Error!!  Retrying...")
        time.sleep(2)
        create_client()

def drawBoard(boardMatrix):
    if boardMatrix[0][0] == -1:
        print("   |", end="")
    elif boardMatrix[0][0] == 0:
        print(" O |", end="")
    elif boardMatrix[0][0] == 1:
        print(" X |", end="")
    
    if boardMatrix[0][1] == -1:
        print("   |", end="")
    elif boardMatrix[0][1] == 0:
        print(" O |", end="")
    elif boardMatrix[0][1] == 1:
        print(" X |", end="")
    
    if boardMatrix[0][2] == -1:
        print("  ")
    elif boardMatrix[0][2] == 0:
        print(" O")
    elif boardMatrix[0][2] == 1:
        print(" X")
    
    print("-----------")
    
    if boardMatrix[1][0] == -1:
        print("   |", end="")
    elif boardMatrix[1][0] == 0:
        print(" O |", end="")
    elif boardMatrix[1][0] == 1:
        print(" X |", end="")
    
    if boardMatrix[1][1] == -1:
        print("   |", end="")
    elif boardMatrix[1][1] == 0:
        print(" O |", end="")
    elif boardMatrix[1][1] == 1:
        print(" X |", end="")
    
    if boardMatrix[1][2] == -1:
        print("  ")
    elif boardMatrix[1][2] == 0:
        print(" O")
    elif boardMatrix[1][2] == 1:
        print(" X")
    
    print("-----------")
    
    if boardMatrix[2][0] == -1:
        print("   |", end="")
    elif boardMatrix[2][0] == 0:
        print(" O |", end="")
    elif boardMatrix[2][0] == 1:
        print(" X |", end="")
    
    if boardMatrix[2][1] == -1:
        print("   |", end="")
    elif boardMatrix[2][1] == 0:
        print(" O |", end="")
    elif boardMatrix[2][1] == 1:
        print(" X |", end="")
    
    if boardMatrix[2][2] == -1:
        print("  ")
    elif boardMatrix[2][2] == 0:
        print(" O")
    elif boardMatrix[2][2] == 1:
        print(" X")
    
def checkWin(boardMatrix):
    res = None
    # check rows
    if boardMatrix[0][0] == boardMatrix[0][1] and boardMatrix[0][0] == boardMatrix[0][2] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
    if boardMatrix[1][0] == boardMatrix[1][1] and boardMatrix[1][0] == boardMatrix[1][2] and boardMatrix[1][0] != -1:
        res = boardMatrix[0][0]
    if boardMatrix[2][0] == boardMatrix[2][1] and boardMatrix[2][0] == boardMatrix[2][2] and boardMatrix[2][0] != -1:
        res = boardMatrix[0][0]

    # check columns
    if boardMatrix[0][0] == boardMatrix[1][0] and boardMatrix[0][0] == boardMatrix[2][0] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
    if boardMatrix[0][1] == boardMatrix[1][1] and boardMatrix[0][1] == boardMatrix[2][1] and boardMatrix[0][1] != -1:
        res = boardMatrix[0][0]
    if boardMatrix[0][2] == boardMatrix[1][2] and boardMatrix[0][2] == boardMatrix[2][2] and boardMatrix[0][2] != -1:
        res = boardMatrix[0][0]

    # check diagonals
    if boardMatrix[0][0] == boardMatrix[1][1] and boardMatrix[0][0] == boardMatrix[2][2] and boardMatrix[0][0] != -1:
        res = boardMatrix[0][0]
    if boardMatrix[0][2] == boardMatrix[1][1] and boardMatrix[0][2] == boardMatrix[2][0] and boardMatrix[0][2] != -1:
        res = boardMatrix[0][0]

    #checkDraw
    if res == None and not (any(-1 in row for row in boardMatrix)):
        return -1
    return res


def communicate():
    global CLIENT
    print('Welcome to Tic-Tac-Toe CLI\n')
    print(" 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n")
    print('Type (1-9) for placing your move\n')
    CLIENT.send(bytes('CONNECT', 'utf-8'))
    incoming_msg = CLIENT.recv(BUFF_SIZE)
    print(incoming_msg.decode('utf-8'))
    
    incoming_msg = CLIENT.recv(BUFF_SIZE)
    incoming_msg = incoming_msg.decode('utf-8')
    if incoming_msg == 'QUIT':
        print('Lost connection with peer!! Quitting...')
        return
    print(incoming_msg)
    player = incoming_msg[-1]

    boardMatrix = [[-1, -1, -1],
                   [-1, -1, -1],
                   [-1, -1, -1]]
    
    if player == 'X':
        drawBoard(boardMatrix)
        self_move = input('Your move > ')
        boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 1
        CLIENT.send(bytes(self_move, 'utf-8'))
        drawBoard(boardMatrix)

    while True:
        print("Waiting for opponent's move...")
        peer_move = CLIENT.recv(BUFF_SIZE)
        if not peer_move:
            print('Disconnected from server!! Quitting...')
            break
        peer_move = peer_move.decode('utf-8')
        if peer_move == '[GAME OVER]':
            peer_move = CLIENT.recv(BUFF_SIZE)
            if player == 'X':
                boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 0
            elif player == 'O':
                boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 1
            drawBoard(boardMatrix)
            print('[GAME OVER]')
            res = checkWin(boardMatrix)
            if res == -1:
                print('----DRAW----')
                break
            print('Oops!! You Lost!!')
            break
        elif peer_move == 'QUIT':
            print('Lost connection with peer!! Quitting...')
            break

        if player == 'X':
            boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 0
        elif player == 'O':
            boardMatrix[(int(peer_move)-1)//3][(int(peer_move)-1)%3] = 1
        drawBoard(boardMatrix)
        
        self_move = input('Your move > ')
        if player == 'X':
            boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 1
        elif player == 'O':
            boardMatrix[(int(self_move)-1)//3][(int(self_move)-1)%3] = 0
        drawBoard(boardMatrix)
        res = checkWin(boardMatrix)

        if res == None:
            CLIENT.send(bytes(self_move, 'utf-8'))
        elif res == -1:
            CLIENT.send(bytes('[GAME OVER]', 'utf-8'))
            print('[GAME OVER]')
            print('----DRAW----')
            CLIENT.send(bytes(self_move, 'utf-8'))
            break
        else:
            CLIENT.send(bytes('[GAME OVER]', 'utf-8'))
            print('[GAME OVER]')
            print('Congrats!! You Win!!')            
            CLIENT.send(bytes(self_move, 'utf-8'))
            break


if __name__ == '__main__':
    create_client()
    communicate()
    CLIENT.close()
    
