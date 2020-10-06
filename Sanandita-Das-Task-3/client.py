import socket

x = "X"
o = "O"

CDASH = str(chr(9532))
VBREAK = " | "
HBREAK = " -"

s = socket.socket()
host = "127.0.0.1"
port = 9998
board = [' '] * 10

s.connect((host, port))

def show_board(board):
    display_line(1, board)
    print(CDASH + HBREAK * 5 + " " + CDASH)
    display_line(4, board)
    print(CDASH + HBREAK * 5 + " " + CDASH)
    display_line(7, board)

def display_line(num, board):
    print("  " + board[num] + VBREAK + board[num+1] + VBREAK + board[num+2] + " ")


def check_win(board):
    x = None
    if board[1] == board[2] and board[1] == board[3]:
        x = board[1]
    elif board[4] == board[5] and board[4] == board[6]:
        x = board[4]
    elif board[7] == board[8] and board[7] == board[9]:
        x = board[7]
    elif board[1] == board[4] and board[1] == board[7]:
        x = board[1]
    elif board[2] == board[5] and board[2] == board[8]:
        x = board[2]
    elif board[3] == board[6] and board[3] == board[9]:
        x = board[3]
    elif board[1] == board[5] and board[1] == board[9]:
        x = board[1]
    elif board[3] == board[5] and board[3] == board[7]:
        x = board[3]


    return x

print('Connected to server.' )

print('YOU ARE PLAYER ', x)

print("The board position numbers")
demo_board = [' '] + [str(i) for i in range(1,10)]
show_board(demo_board)

while True:
    try:
        print('\nwait for player', o)
        pos = int(s.recv(1024).decode('utf-8'))
        board[pos] = o
        show_board(board)
        
        if check_win(board) == None and board.count(' ') == 1:
            print('<<<<THE GAME IS DRAW>>>>')
            s.close()
            break
        elif check_win(board) != ' ' and check_win(board) != None:
            print('Player', check_win(board), 'wins :)')
            s.close()
            break
        
        
        else:
            while True:
                pos = int(input('\n YOUR TURN>>> '))
                if 1 > pos or 9 < pos:
                    print('Invalid choice...')
                    continue
                elif board[pos] != ' ':
                    print('Already occupied... RETRY>>>')
                else:
                    break
            board[pos] = x
            show_board(board)

            if check_win(board) == None and board.count(' ') == 1:
                s.send(str(pos).encode('utf-8'))
                print('<<<<THE GAME IS DRAW>>>>') # if no one wins
                s.close()
                break
            elif check_win(board) != ' ' and check_win(board) != None:
                s.send(str(pos).encode('utf-8'))
                print("Player", check_win(board), 'wins :)') # someone win
                s.close()
                break
            else:
                s.send(str(pos).encode('utf-8'))
    except:
        s.close()
        
