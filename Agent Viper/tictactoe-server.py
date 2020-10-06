import socket
import sys

c = 0
check = 0
a = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def draw():
    global a
    for i in range(3):
        # for j in range(3):
        # print('|' + str(a[i][j]) + '|')
        print(str(a[i][0]), '|', str(a[i][1]), '|', str(a[i][2]))
        if i != 2:
            print('----------')


def filling(response, ch):
    flag = 0
    global a, check
    if response >= 1 and response <= 9:
        for i in range(3):
            for j in range(3):
                flag += 1
                if flag == response:
                    if str(a[i][j]) == 'X' or str(a[i][j]) == 'O':
                        check = 1
                    else:
                        a[i][j] = ch
    else:
        check = 1


def helper(conn):
    while True:
        global check, c
        check_win(conn)
        if c == 9:
            print('DRAW!')
            conn.close()
            s.close()
            sys.exit()
        if c % 2 == 0:
            res = input('Enter next move: ')
            conn.sendall(res.encode('utf-8'))
            res = int(res)
            filling(res, 'X')

        else:
            print('Opponent plays: ')
            t = conn.recv(1024).decode('utf-8')
            t = int(t)
            filling(t, 'O')

        if check == 1 and c % 2 == 0:
            print('Incorrect position! ')
            check = 0
            continue
        elif check == 1 and c % 2 != 0:
            print('Opponent selected an incorrect position')
            check = 0
            continue
        draw()
        c += 1


def check_win(conne):
    global c
    g = 0
    if a[0][0] == a[0][1] and a[0][0] == a[0][2] and (a[0][0] == 'X' or a[0][0] == 'O'):
        g = 1
    elif a[1][0] == a[1][1] and a[1][0] == a[1][2] and (a[1][0] == 'X' or a[1][0] == 'O'):
        g = 1
    elif a[2][0] == a[2][1] and a[2][0] == a[2][2] and (a[2][0] == 'X' or a[2][0] == 'O'):
        g = 1
    elif a[0][1] == a[1][1] and a[0][1] == a[2][1] and (a[0][1] == 'X' or a[0][1] == 'O'):
        g = 1
    elif a[0][0] == a[1][0] and a[0][0] == a[2][0] and (a[0][0] == 'X' or a[0][0] == 'O'):
        g = 1
    elif a[0][2] == a[1][2] and a[0][2] == a[2][2] and (a[0][2] == 'X' or a[0][2] == 'O'):
        g = 1
    elif a[0][0] == a[1][1] and a[0][0] == a[2][2] and (a[0][0] == 'X' or a[0][0] == 'O'):
        g = 1
    elif a[0][2] == a[1][1] and a[0][2] == a[2][0] and (a[1][1] == 'X' or a[1][1] == 'O'):
        g = 1
    if c % 2 != 0 and g == 1:
        print('You win!')
        conne.close()
        s.close()
        sys.exit()
    elif c % 2 == 0 and g == 1:
        print('You lose!')
        conne.close()
        s.close()
        sys.exit()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

host = '127.0.0.1'
port = 1234

s.bind((host, port))
print('socket bound to ' + str(host) + ' : ' + str(port))

s.listen(5)
print('listening')

con, address = s.accept()
print('Connected to ', address)

print('''
To make a move, enter a number from 1-9
1 2 3
4 5 6
7 8 9\nYou are player X''')
helper(con)
