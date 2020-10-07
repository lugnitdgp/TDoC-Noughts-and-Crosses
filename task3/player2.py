import socket
import emoji
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9091

s.connect((host, 9090))
res = s.recv(1024)
print(res.decode("utf-8"))
game = True
b = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def board_player2(a):
    global b
    c = int(a % 3)
    r = int(a/3)
    if b[r][c] != 'X' and b[r][c] != 'O':
        b[r][c] = 'O'
        display()
        return True
    else:
        print("Wrong Move enter again")
        return False


def board_player1(a):
    global b
    c = a % 3
    r = int(a / 3)
    b[r][c] = 'X'


def display():
    global b
    p = 0
    q = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if b[i][j] == 'X':
                print(emoji.emojize(":x:",use_aliases=True), end="")
            elif b[i][j] == 'O':
                print(emoji.emojize(":o:",use_aliases=True), end="")
            else:
                print(b[i][j], end="")
            if j != 2:
                print(" | ", end ="")
            else:
                print("")
        if i != 2:
            print("----------")
        else:
            print("")


def Check():
    global b
    if b[0][0] == b[0][1] and b[0][1] == b[0][2] and b[0][0] != ' ':       # checking left and right
        if b[0][0] == 'X':
            return 1
        else:
            return 2
    if b[1][0] == b[1][1] and b[1][1] == b[1][2] and b[1][0] != ' ':
        if b[1][0] == 'X':
            return 1
        else:
            return 2
    if b[2][0] == b[2][1] and b[2][1] == b[2][2] and b[2][0] != ' ':
        if b[2][0] == 'X':
            return 1
        else:
            return 2
    if b[0][0] == b[1][0] and b[1][0] == b[2][0] and b[0][0] != ' ':        # checking down and up
        if b[0][0] == 'X':
            return 1
        else:
            return 2
    if b[0][1] == b[1][1] and b[1][1] == b[2][1] and b[0][1] != ' ':
        if b[0][1] == 'X':
            return 1
        else:
            return 2
    if b[0][2] == b[1][2] and b[1][2] == b[2][2] and b[0][2] != ' ':
        if b[0][2] == 'X':
            return 1
        else:
            return 2
    if b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[0][0] != ' ':            # checking diagonals
        if b[0][0] == 'X':
            return 1
        else:
            return 2
    if b[0][2] == b[1][1] and b[1][1] == b[2][0] and b[0][2] != ' ':
        if b[0][2] == 'X':
            return 1
        else:
            return 2
    return -1


moves = 0
flag = 0
display()

while game and moves < 9:
    res = s.recv(8)
    res = res.decode("utf-8")
    moves += 1
    board_player1(int(res))
    p = Check()
    display()
    if p == 1:
        print("Player1 won....")
        s.close()
        break
    if moves == 9:
        break
    print("Enter between 1-9 to add a valid move in the board : ")
    Input = int(input())
    while not board_player2(Input-1):
        Input = int(input())
    moves += 1
    p = Check()
    if moves == 9:
        s.sendto(str.encode(str(Input - 1)), (host, 9090))
        break
    if p == 2:
        msg = "Player2 won...."
        flag = 1
        s.sendto(str.encode(str(Input-1)), (host, 9090))
        print(msg)
        s.close()
        break
    else:
        s.sendto(str.encode(str(Input-1)), (host, 9090))
if moves == 9 and flag == 0:
    print("Draw!")
    s.close()
