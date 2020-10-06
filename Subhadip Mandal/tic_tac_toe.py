def create_board():
    board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
        }
    return board


def print_board_layout():
    print('''
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
''')


def print_start_msg():
    print('This is the board layout.\nTo give move at a position, enter the number at that position.')
    print_board_layout()
    print('Game started.')


def print_current_board_state(board):
    print(f"""
 {board['1']} | {board['2']} | {board['3']} 
---+---+---
 {board['4']} | {board['5']} | {board['6']}
---+---+---
 {board['7']} | {board['8']} | {board['9']}
""")


def check(board):
    if board['1'] == board['2'] == board['3'] == 'X':
        return 1
    if board['4'] == board['5'] == board['6'] == 'X':
        return 1
    if board['7'] == board['8'] == board['9'] == 'X':
        return 1
    if board['1'] == board['4'] == board['7'] == 'X':
        return 1
    if board['2'] == board['5'] == board['8'] == 'X':
        return 1
    if board['3'] == board['6'] == board['9'] == 'X':
        return 1
    if board['1'] == board['5'] == board['9'] == 'X':
        return 1
    if board['3'] == board['5'] == board['7'] == 'X':
        return 1

    if board['1'] == board['2'] == board['3'] == 'O':
        return 2
    if board['4'] == board['5'] == board['6'] == 'O':
        return 2
    if board['7'] == board['8'] == board['9'] == 'O':
        return 2
    if board['1'] == board['4'] == board['7'] == 'O':
        return 2
    if board['2'] == board['5'] == board['8'] == 'O':
        return 2
    if board['3'] == board['6'] == board['9'] == 'O':
        return 2
    if board['1'] == board['5'] == board['9'] == 'O':
        return 2
    if board['3'] == board['5'] == board['7'] == 'O':
        return 2


def move(board, player):
    if player == 1:
        while True:
            p1_input = input("Your move: ")
            if p1_input in board and board[p1_input] == ' ':
                board[p1_input] = "X"
                print_current_board_state(board)
                break
            else:
                print('Invalid move. Try again.')
                continue
        return board, p1_input

    if player == 2:
        while True:
            p2_input = input("Your move: ")
            if p2_input in board and board[p2_input] == ' ':
                board[p2_input] = "O"
                print_current_board_state(board)
                break
            else:
                print('Invalid move. Try again.')
                continue
        return board, p2_input


def update_board(board, player, opponent_move):
    if player == 1:
        board[opponent_move] = 'O'
    if player == 2:
        board[opponent_move] = 'X'
    return board


