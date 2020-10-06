import socket
from tic_tac_toe import *

host = "127.0.0.1"
port = 9898
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

board = create_board()
total_move = 0
print_start_msg()

while True:
    print("Waiting for opponent's move...")
    p1_move = (s.recv(1024))
    board = update_board(board, 2, p1_move.decode('utf-8'))
    total_move += 1
    print_current_board_state(board)
    if check(board) == 1:
        print('*** You lost the match. ***')
        s.close()
        break

    if total_move == 9:
        print('*** Match draw. ***')
        s.close()
        break

    board, p2_move = move(board, 2)
    total_move += 1
    s.send(p2_move.encode('utf-8'))

    if check(board) == 2:
        print('*** You won the match. ***')
        s.close()
        break











