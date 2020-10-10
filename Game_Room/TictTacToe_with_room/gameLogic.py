import sys
import emoji

HDASH = chr(9474)
VDASH = chr(9472)
CDASH = chr(9532)

def horiz_line():
    resp = ''
    for _ in range(4):
        resp += VDASH
    resp+=CDASH
    for _ in range(4):
        resp += VDASH
    resp+=CDASH
    for _ in range(4):
        resp += VDASH
    return resp

def row_string(brd):
    disp = ''
    if brd[0]==0:
        disp += ' '*4
    elif brd[0]==1:
        disp += emoji.emojize(' :cross_mark: ')
    else:
        disp += emoji.emojize(' :white_circle: ')

    disp += HDASH

    if brd[1]==0:
        disp += ' '*4
    elif brd[1]==1:
        disp += emoji.emojize(' :cross_mark: ')
    else:
        disp += emoji.emojize(' :white_circle: ')

    disp += HDASH

    if brd[2]==0:
        disp += ' '*4
    elif brd[2]==1:
        disp += emoji.emojize(' :cross_mark: ')
    else:
        disp += emoji.emojize(' :white_circle: ')

    return disp


class TicTacToe:
    def __init__(self, id):
        self.board = [0]*9
        self.id = id

    def p1_move(self, pos=-1):
        while True:
            try:
                if pos==-1:
                    pos = int(input('[PLAYER 1\'s MOVE]: '))
                if self.board[pos]==0:
                    self.board[pos]=1
                    return pos
                else:
                    pos=-1
                    print('[PLEASE TRY AGAIN :( ]')
            except:
                pos=-1
                print('[PLEASE TRY AGAIN :( ]')
                pass

    def p2_move(self, pos=-1):
        while True:
            try:
                if pos==-1:
                    pos = int(input('[PLAYER 2\'s MOVE]: '))
                if pos<9 and pos>=0 and self.board[pos]==0:
                    self.board[pos]=-1
                    return pos
                else:
                    pos=-1
                    print('[PLEASE TRY AGAIN :( ]')
            except:
                pos=-1
                print('[PLEASE TRY AGAIN :( ]')
                pass

    def isGameOver(self, lpos):
        win = self.find_winner(lpos)
        if win == self.id:
            print(emoji.emojize(':party_popper: [CONGO !! YOU WON] :party_popper:'))
            return win
        elif win:
            print(emoji.emojize('[OOPS !! YOU LOST] :pensive_face:'))
            return win
        else:
            for i in range(9):
                if self.board[i]==0:
                    return 0
            print('==[THE GAME WAS A DRAW]==')
            return -1


    # 0 -> Not ovee 1-> p1 won 2-> p2 won -1-> draw

    def find_winner(self, lpos):
        brd = self.board
        assert(lpos<9 and lpos>=0)
        row = lpos//3
        col = lpos%3
        
        # checking rows
        tot=0
        for r in range(3):
            tot += brd[3*row + r]
        if tot==3:
            return 1
        elif tot==-3:
            return 2

        #  checking columns
        tot=0
        for c in range(3):
            tot += brd[c*3+col]

        if tot==3:
            return 1
        elif tot==-3:
            return 2

        # checking diag
        if row==col:
            tot=0
            tot += brd[0]
            tot += brd[4]
            tot += brd[8]

            if tot==3:
                return 1
            elif tot==-3:
                return 2

        # checking anti-diag
        if row+col==2:
            tot=0
            tot += brd[2]
            tot += brd[4]
            tot += brd[6]

            if tot==3:
                return 1
            elif tot==-3:
                return 2

        return 0

    def display_board(self):
        brd = self.board
        disp = ''
        disp += row_string([brd[0], brd[1], brd[2]])
        disp += '\n'
        disp += horiz_line()
        disp += '\n'
        disp += row_string([brd[3], brd[4], brd[5]])
        disp += '\n'
        disp += horiz_line()
        disp += '\n'
        disp += row_string([brd[6], brd[7], brd[8]])
        disp += '\n'
        print('[BOARD]: \n')
        print(disp)
        print()
        



        

# def main():
#     game = TicTacToe()
#     for _ in range(9):
#         lmove = game.p1_move()
#         game.display_board()
#         result = game.isGameOver(lmove)

#         if result!=0:
#             sys.exit(0)
#             # break
        
#         lmove = game.p2_move()
#         game.display_board()
#         result = game.isGameOver(lmove)

#         if result!=0:
#             sys.exit(0)  

# main()