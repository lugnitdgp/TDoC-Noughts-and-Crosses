# IT IS THE SERVER FILE SO PLEASE RUN IT FIRST


import socket
import emoji
global x
global o


x = emoji.emojize(':heavy_multiplication_x:') + ' '
o = emoji.emojize(':white_circle:')
board = ['  ']*10

# CREATING SOCKET
def create_socket():
    try:
        global host
        global port
        global s
        host = ""  # Standard interface address (localhost)
        port = 9998  # Port to listen on (non-privileged ports are > 1023)

        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error:", msg)


# BINDING THE PORT WITH SOCKET AND LISTENING FOR CONNECTION
def binding_socket():
    global host
    global port
    global s

    print("Binding the port:", port)

    try:
        s.bind((host, port))
        # It has a backlog parameter. Specify the number of connections to allow simulatneously
        s.listen(5)

    except socket.error as msg:
        print('socket binding error:', msg)
        print('retrying...')

        # if the socket fails to bind or listen, then retry...
        binding_socket()


# ACCEPTING FROM CLIENT
def socket_accept():
    # connection is a socket object that has various functions to execute
    connection, address = s.accept()
    # system calls like send(), recv()

    print("Connection has been established! | IP",
          address[0], ' | PORT', address[1])
    print('Let\'s play>>>')
    print('NOTE: You are player ', o)
    show_board(board)
    play(connection, board)



# TO PRINT THE BOARD
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


# playing the game here
def play(connection, board):
    board = ['  ']*10
    try:
        while True:
            while True:  # validation of the entered choice
                pos = int(input('\n YOUR TURN>>> '))
                if 1 > pos or 9 < pos
                    print('Invalid choice....')
                    continue
                elif board[pos] != '  ':
                    print('Already occupied... RETRY>>>')
                else:
                    break
            board[pos] = o
            show_board(board)

            # checking who win 
            if check_win(board) == None and board.count('  ') == 1:
                connection.send(str(pos).encode('utf-8'))
                print('<<<<THE GAME IS DRAW>>>>')
                connection.close() # if no one wins
                break
            elif check_win(board) != '  ' and check_win(board) != None:
                connection.send(str(pos).encode('utf-8'))
                print("Player", check_win(board), 'wins :)')
                connection.close() # someone win
                break
            else:
                connection.send(str(pos).encode('utf-8'))


            # Waiting for the response of second friend
            print('\nwait for player', x)
            pos = int(connection.recv(1024).decode('utf-8'))
            board[pos] = x
            show_board(board)

            if check_win(board) == None and board.count('  ') == 1:
                print('<<<<THE GAME IS DRAW>>>>')
                connection.close()
                break
            elif check_win(board) != '  ' and check_win(board) != None:
                print('Player', check_win(board), 'wins :)')
                connection.close()
                break
            else:
                continue
    except:
        connection.close()



def main():
    create_socket()
    binding_socket()
    socket_accept()


main()
