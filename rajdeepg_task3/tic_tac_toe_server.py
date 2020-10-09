import socket

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

# MAIN LOGIC OF THE CODE

def logic(obj):
    board = [['---', '---', '---'],
             ['---', '---', '---'], ['---', '---', '---']]
    distinct = set()
    flag = False

    print("The Positions Of each Block Are Given !! ", end="\n\n")
    # board_rule(board)
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(' ' + str(3*i+j+1) + ' ' + '|', end="")
        print("\n")

    while (len(distinct) < 9):


        print("Enter Your Position (Betwen to 1 to 9 ): ", end="")
        num = int(input())
        num -= 1

        if(num < 0 or num > 8):
            print("Invalid Input", end="\n\n")
            continue

        if(num in distinct):
            print("Sorry!!! The Position you entered is already occupied.", end="\n")
            continue

        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' X '

        print("\n")
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(board[i][j] + '|', end="")
            print("\n")

        obj.sendall(str(num).encode("utf-8"))

        if(check_win(board)):
            print("Congratulations ! YOU HAVE WON THE GAME")
            flag = True
            break

        print("Waiting for the other player to Reply...", end="\n\n")

        num = int(obj.recv(1024).decode("utf-8"))
        distinct.add(num)
        row = (num//3)
        col = num % 3
        board[row][col] = ' O '

        print("It'your turn to make your move !!!", end="\n\n")
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(board[i][j] + '|', end="")
            print("\n")
        
        if(check_win(board)):
            print("YOU LOST :(")
            flag = True
            break

    if(flag == False):
        print("ITS A DRAW")

# MAIN FUNCTION

def main():
    try:
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(msg)    

    try:
        s.bind((host, port))
        s.listen(5)
    except:
        print("Could Not Bind To The Port " + str(port) + " Retrying...")
    
    print('Waiting for connection..............................')
    obj, address = s.accept()
    print("Connection Established --- IP : " + address[0] + " Port : " + str(address[1]))
    logic(obj)
    
    
    obj.close()

main()