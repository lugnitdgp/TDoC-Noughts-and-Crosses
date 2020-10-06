import socket

x = "X"
o = "O"
CDASH = str(chr(9532))
VBREAK = " | "
HBREAK = " -"

def create_socket(host, port):
    try:
        s = socket.socket()
        return s
    except socket.error as msg:
        print("Socket creation error:", msg)
            
def binding_socket(host, port, s):
    print("Binding the port:", port)
    try:
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print('socket binding error:', msg)
        print('retrying...')
        binding_socket()                          
        
def socket_accept(s):
    connection, address = s.accept()
    
    print("Connected with :", address)
    print('You are player ', o)
    return connection

def show_board(board):
    display_line(1, board)
    print(CDASH + HBREAK * 5 + " " + CDASH)
    display_line(4, board)
    print(CDASH + HBREAK * 5 + " " + CDASH)
    display_line(7, board)
        
def display_line(num, board):
    print("  " + board[num] + VBREAK + board[num+1] + VBREAK + board[num+2] + " ")

def check_win(board):
    x =  None
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
 
                                                                                    
def move(connection, board):                                                                              
    try:
        while True:
            while True:  # validation of the entered choice
                pos = int(input('\n YOUR TURN>>> '))
                if 1 > pos or 9 < pos:
                    print('Invalid choice....')
                    continue
                elif board[pos] != ' ':
                    print('Already occupied... RETRY>>>')
                else:
                    break
            board[pos] = o
            show_board(board)
            # checking who win
            if check_win(board) == None and board.count(' ') == 1:
                connection.send(str(pos).encode('utf-8'))
                print('<<<<THE GAME IS DRAW>>>>')
                connection.close() # if no one wins
                break
            elif check_win(board) != ' ' and check_win(board) != None:
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

            if check_win(board) == None and board.count(' ') == 1:
                print('<<<<THE GAME IS DRAW>>>>')
                connection.close()
                break
            elif check_win(board) != ' ' and check_win(board) != None:
                print('Player', check_win(board), 'wins :)')
                connection.close()
                break
            else:
                continue
    except:
        connection.close()
    
def main():
    host  = "127.0.0.1"
    port = 9998
    s = create_socket(host, port)
    binding_socket(host, port, s)
    connection = socket_accept(s)
    print("The board position numbers")
    demo_board = [' '] + [ str(i) for i in range(1,10)]
    show_board(demo_board)
    board = [' '] * 10
    move(connection,board)

main()
