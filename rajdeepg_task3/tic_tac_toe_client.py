import socket

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 9999


s.connect((host, port))

def check_win(board):
    for i in range(3):
        ch = board[i][0]
        f = True
        for j in range(1, 3):
            if(board[i][j] != ch or board[i][j] == '---'):
                f = False
                break
        if(f == True):
            return True
    for i in range(3):
        ch = board[0][i]
        f = True
        for j in range(1, 3):
            if(board[j][i] != ch or board[j][i] == '---'):
                f = False
                break
        if(f == True):
            return True
    if((board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '---') or (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != '---')):
        return True
    return False

# The Main Program Goes Here 

def main():
    board = [['---', '---', '---'],
            ['---', '---', '---'], ['---', '---', '---']]
    distinct = set()
    flag = False

    print("The Positions Of each Block Are Given !! ")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(' ' + str(3*i+j+1) + ' ' + '|', end="")
        print("\n")

    while (len(distinct) < 9):

        print("Waiting For X to Reply...", end="\n\n")

        num = int(s.recv(1024).decode("utf-8"))
        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' X '

        if(len(distinct) == 9):
            print("The other player has made its move")
            for i in range(3):
                print("|", end="")
                for j in range(3):
                    print(board[i][j] + '|', end="")
                print("\n")
            break

        print("Now its your turn", end="\n\n")
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(board[i][j] + '|', end="")
            print("\n")

        if(check_win(board)):
            print("You LOST :/")
            flag = True
            break

        print("Enter Your Position (Betwen to 1 to 9 ): ", end="")
        num = int(input())
        num -= 1

        if(num < 0 or num > 8):
            print("Invalid Input", end="\n\n")
            continue

        if(num in distinct):
            print("Sorry!!! The Position you entered is already occupied.", end="\n\n")
            continue

        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' O '

        print("\n")
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(board[i][j] + '|', end="")
            print("\n")

        s.sendall(str(num).encode("utf-8"))

        if(check_win(board)):
            print("Congratulations ! YOU HAVE WON THE GAME")
            flag = True
            break
    if(flag == False):
        print("ITS A DRAW")

main() 