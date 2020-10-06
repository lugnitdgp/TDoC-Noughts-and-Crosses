import socket

# Creating The Basic Board


def board_display(board):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j] + '|', end="")
        print("\n")

# Assigning Numbers To The Positions


def board_rule(board):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(' ' + str(3*i+j+1) + ' ' + '|', end="")
        print("\n")

# Function For Checking The Win


def check_win(board):
    for i in range(3):
        ch = board[i][0]
        f = True
        for j in range(1, 3):
            if(board[i][j] != ch or board[i][j] == '----'):
                f = False
                break
        if(f == True):
            return True
    for i in range(3):
        ch = board[0][i]
        f = True
        for j in range(1, 3):
            if(board[j][i] != ch or board[j][i] == '----'):
                f = False
                break
        if(f == True):
            return True
    if((board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '----') or (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != '----')):
        return True
    return False

# Defining The Host and Port And Creating A Socket


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(msg)

# Binding The Socket With Port And Listening


def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(5)
    except:
        print("Could Not Bind To The Port " + str(port) + " Retrying...")
        bind_socket()

# Accepting THe Connection


def accept_client():
    conn, address = s.accept()
    print("Connection Established --- IP : " +
          address[0] + " Port : " + str(address[1]))
    command(conn)
    conn.close()

# The Main Task Goes Here


def command(conn):
    board = [['----', '----', '----'],
             ['----', '----', '----'], ['----', '----', '----']]
    distinct = set()
    flag = False

    print("The Positions Of each Block Are Given !! ", end="\n\n")
    board_rule(board)

    while (len(distinct) < 9):

        # Server Response And Sending Data To Client

        print("Enter Your Position : ", end="")
        num = int(input())
        num -= 1

        if(num < 0 or num > 8):
            print("Invalid Input", end="\n\n")
            continue

        if(num in distinct):
            print("Woops ! The Position Is Already Taken !!", end="\n\n")
            board_display(board)
            continue

        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' ❌ '

        print("\n")
        board_display(board)

        conn.sendall(str(num).encode("utf-8"))

        if(check_win(board)):
            print("Congratulations ! You Won The Game !")
            flag = True
            break

        print("Waiting For ⭕ to Reply...", end="\n\n")

        # Client Response

        num = int(conn.recv(1024).decode("utf-8"))
        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' ⭕ '

        print("⭕ Has made His Move ! It's Your Turn !", end="\n\n")
        board_display(board)

        if(check_win(board)):
            print("You Lost The Game ! Sorry !")
            flag = True
            break

    # Checking For Draw Condition
    if(flag == False):
        print("Ohh ! The Game Ended In A Draw !")


def main():
    create_socket()
    bind_socket()
    accept_client()


main()
