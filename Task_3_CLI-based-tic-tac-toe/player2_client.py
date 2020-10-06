import socket
global x
global o

x = 'X'
o = 'O'
board = ['  ']*10

s = socket.socket()
host = socket.gethostname()
port = 5000  
s.connect((host, port)) 

# for printing the board
def show_board(board):
    print(board[1], '|', board[2], '|', board[3])
    print('-'*12)
    print(board[4], '|', board[5], '|', board[6])
    print('-'*12)
    print(board[7], '|', board[8], '|', board[9])

# Check who wins after each turn 
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

print('Connected to server: start playing>>>' )

print('you the', x,'player')

while True:
    try:

        # waiting for the response of first friend
        print('\nwaiting for player', o)
        pos = int(s.recv(1024).decode('utf-8'))
        board[pos] = o
        show_board(board)

        if check_win(board) == None and board.count('  ') == 1:
            print('!!!DRAW!!!')
            s.close()
            break
        elif check_win(board) != '  ' and check_win(board) != None:
            print('Player', check_win(board), 'wins :)')
            s.close()
            break
        else:
            while True: 
                pos = int(input('\n Enter your choice--->> '))
                if 1 > pos or 9 < pos:
                    print('Invalid choice!!')
                    continue
                elif board[pos] != '  ':
                    print('Already taken... try again--->>')
                else:
                    break
            board[pos] = x
            show_board(board)

       
            if check_win(board) == None and board.count('  ') == 1:
                s.send(str(pos).encode('utf-8'))
                print('!!!DRAW!!!') 
                s.close()
                break
            elif check_win(board) != '  ' and check_win(board) != None:
                s.send(str(pos).encode('utf-8'))
                print("Player", check_win(board), 'wins :)') 
                s.close()
                break
            else:
                s.send(str(pos).encode('utf-8'))
    except:
        s.close()
