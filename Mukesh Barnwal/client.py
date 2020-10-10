import socket        
import threading
from game import game

HEADER = 64
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)             
HOST = socket.gethostbyname(socket.gethostname())
PORT = 50001
s.bind((HOST, PORT))   

game = game()
choice = ['0', 'X']
turn = 0

print('||--------------You are The Player X--------------||', end='\n\n')
print('To make a move, enter a number from 1-9')
for x in range(1,10):
    print(x, end=' ')
    if x%3==0:
        print('')

for i in range(9):
    x=0
    if turn==0:
        print('Waiting for other player to move :')
        x = s.recv(64).decode(FORMAT)
    else:
        print('enter the next move :', end=' ')
        x = input()
        s.sendto(x.encode(FORMAT), (HOST, 50000))
    
    game.put(int(x), choice[turn])
    res = game.check()
    game.print_board()

    if res is not None:
        if turn==0:
            print('Player 0 wins.')
        else:
            print('You wins.')
        break
    if i==8:
        print('Match Draw.')
    
    turn ^= 1



    

        

