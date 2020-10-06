import socket
from tic_tac_toe import *

host = "127.0.0.1"
port = 9898
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print('Waiting for opponent to connect.')
conn, addr = s.accept()
print(f'Opponent connected. | IP: {addr[0]} | Port: {addr[1]}')

board = create_board()
total_move = 0
print_start_msg()
print_current_board_state(board)

while True:
    board, p1_move = move(board, 1)
    total_move += 1
    conn.send(p1_move.encode('utf-8'))

    if total_move == 9:
        print('*** Match draw. ***')
        conn.close()
        s.close()
        break

    if check(board) == 1:
        print('*** You won the match. ***')
        conn.close()
        s.close()
        break

    print("Waiting for opponent's move...")
    p2_move = (conn.recv(1024))
    board = update_board(board, 1, p2_move.decode('utf-8'))
    total_move += 1

    print_current_board_state(board)
    if check(board) == 2:
        print('*** You lost the match. ***')
        conn.close()
        s.close()
        break




