# IT'S YOUR FRIEND WORK IF THE CLIENT1 IS LISTENING


import socket
import emoji
global x
global o

x = emoji.emojize(':heavy_multiplication_x:') + ' '
o = emoji.emojize(':white_circle:')
board = ['  ']*10

s = socket.socket()
host = "172.20.10.2"


'''
THIS IS THE IP ADDRESS OF THE HOST. IN OUR CASE WE HAVE USED THE IP ADDRESS EXPLICITLY.

ONCE THE VM IS READY AND HOST IS PLACED THERE, THE IP ADRESS OF THE SERVER WILL GO IN HERE AS IT WILL BE STATIC

'''

port = 9998  # Port to listen on (non-privileged ports are > 1023)

s.connect((host, port))  # binding the socket in client file

# TO PRINT THE BOARD

# for printing the board
def show_board(board):
    print(board[1], '|', board[2], '|', board[3])
    print('-'*12)
    print(board[4], '|', board[5], '|', board[6])
    print('-'*12)
    print(board[7], '|', board[8], '|', board[9])

# Checking who wins. It return None: if draw else X or O
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

print('Connected to server: Let\'s play>>>' )

print('NOTE:  YOU ARE PLAYER ', x)

while True:
    try:

        # waiting for the response of first friend
        print('\nwait for player', o)
        pos = int(s.recv(1024).decode('utf-8'))
        board[pos] = o
        show_board(board)

        # checking who wins
        if check_win(board) == None and board.count('  ') == 1:
            print('<<<<THE GAME IS DRAW>>>>')
            s.close()
            break
        elif check_win(board) != '  ' and check_win(board) != None:
            print('Player', check_win(board), 'wins :)')
            s.close()
            break





        else:
            while True: # validation of the entered choice
                pos = int(input('\n YOUR TURN>>> '))
                if 1 > pos or 9 < pos:
                    print('Invalid choice...')
                    continue
                elif board[pos] != '  ':
                    print('Already occupied... RETRY>>>')
                else:
                    break
            board[pos] = x
            show_board(board)

            # Check who wins
            if check_win(board) == None and board.count('  ') == 1:
                s.send(str(pos).encode('utf-8'))
                print('<<<<THE GAME IS DRAW>>>>') # if no one wins
                s.close()
                break
            elif check_win(board) != '  ' and check_win(board) != None:
                s.send(str(pos).encode('utf-8'))
                print("Player", check_win(board), 'wins :)') # someone win
                s.close()
                break
            else:
                s.send(str(pos).encode('utf-8'))
    except:
        s.close()
        








