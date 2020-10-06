import socket

# Creating Socket And Defining Host and Port Name

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 9999

# Establishing Connection

s.connect((host, port))

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

# The Main Program Goes Here 

def main():
    board = [['----', '----', '----'],
            ['----', '----', '----'], ['----', '----', '----']]
    distinct = set()
    flag = False

    print("The Positions Of each Block Are Given !! ")
    board_rule(board)

    while (len(distinct) < 9):

        print("Waiting For ❌ to Reply...", end="\n\n")

        # Server Response

        num = int(s.recv(1024).decode("utf-8"))
        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' ❌ '

        if(len(distinct) == 9):
            print("❌ has made Their Move")
            board_display(board)
            break

        print("❌ has made his Move ! Now It's Your Turn !", end="\n\n")
        board_display(board)

        if(check_win(board)):
            print("You Lost The Game ! Sorry !")
            flag = True
            break

        # Client Response And Sending Data To Server 

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
        board[row][col] = ' ⭕ '

        print("\n")
        board_display(board)

        s.sendall(str(num).encode("utf-8"))

        if(check_win(board)):
            print("Congratulations ! You Won The Game !")
            flag = True
            break

    # Checking For Draw Condition

    if(flag == False):
        print("Ohh ! The Game Ended In A Draw !")

main()