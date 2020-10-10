import pygame
import os
import threading
import socket
import tkinter
from tkinter import messagebox







os.environ['SDL_VIDEO_WINDOW_POS'] = '850,100'  # SETTING THE POSITION OF STARTING OF BOARD
letterX = pygame.image.load(os.path.join('x.png'))  # LOADING AND SCALING IMAGES
letterX = pygame.transform.scale(letterX, (200, 200))
letterO = pygame.image.load(os.path.join('o.jpg'))
letterO = pygame.transform.scale(letterO, (200, 200))
back = pygame.image.load(os.path.join('back.jpeg'))
back = pygame.transform.scale(back, (600, 600))

surface = pygame.display.set_mode((600,600)) # STARTING A SQUARE BOX
pygame.display.set_caption('Tic Tac Toe')







# create a separate thread to send and receive data from the server
def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()






# CLASS FOR DEFINING ALL THE FUNCTIONS RELATED TO Board PROCESSING
class Board:
    def __init__(self):
        self.Board_lines = [((0,200), (600,200)), ((0,400), (600,400)), ((200,0), (200,600)),((400,0), (400,600))]
        # THESE NUMBERS ARE THE PAIR OF STARTING AND CLOSING COORDINATES OF INDIVIDUAL LINES

        self.Board = [[0 for x in range(3)] for y in range(3)] # OUR MAIN Board
        # search directions         s         sw        W       nw        n       ne      e       se
        self.direction_to_move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.game_over = False



    # THE PRINCIPLE METHOD TO CHECK FOR WINNING OR DRAWING. IT USES A DIRECTIONAL APPROACH TO CHECK THE ELEMENTS
    def check_Board(self, x, y, player):
        count = 1
        for index, (dx, dy) in enumerate(self.direction_to_move):
            if self.is_possible(x + dx, y + dy) and self.get_cell_value(x + dx, y + dy) == player:
                count += 1
                xx = x + dx
                yy = y + dy
                if self.is_possible(xx + dx, yy + dy) and self.get_cell_value(xx + dx, yy + dy) == player:
                    count += 1
                    if count == 3:
                        break

                # THE CASE WHEN A CORNER IS THERE AND IT STILL COUNTS 3 BUT THE ORIGINAL ELEMENTS WILL BE 2 OR CAN BE THE CASE WITH 2 AND 1 ALSO
                if count < 3:
                    reversed_direction = 0

                    # REVERSING THE DIRECTION TO GO TO THE OPPOSITE SIDE OF WHAT WE CHECKED BEFORE CAN MORE BE UNDERSTOOD IN NOTES I WILL ATTACH
                    if index == 0:        
                        reversed_direction = self.direction_to_move[4] # N to S
                    elif index == 1:
                        reversed_direction = self.direction_to_move[5] # NW to SE
                    elif index == 2:
                        reversed_direction = self.direction_to_move[6] # W to E
                    elif index == 3:
                        reversed_direction = self.direction_to_move[7] # SW to NE
                    elif index == 4:
                        reversed_direction = self.direction_to_move[0] # S to N
                    elif index == 5:
                        reversed_direction = self.direction_to_move[1] # SE to NW
                    elif index == 6:
                        reversed_direction = self.direction_to_move[2] # E to W
                    elif index == 7:
                        reversed_direction = self.direction_to_move[3] # NE to SW

                    if self.is_possible(x + reversed_direction[0], y + reversed_direction[1]) and self.get_cell_value(x + reversed_direction[0], y + reversed_direction[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1 # TO CONTINUE AGAIN

        if count == 3:

            # POP-UP FOR WINNING
            root = tkinter.Tk()
            ws = root.winfo_screenwidth() # width of the screen
            hs = root.winfo_screenheight() # height of the screen
            msg = str(player) + ' wins!!'
            root.geometry('%dx%d+%d+%d' % (200, 200, (2*ws)//3, hs//2))
            tkinter.messagebox.showinfo('Alert', msg)
            root.destroy()
            print(player, 'wins!')
            self.game_over = True
            self.instructions()
        else:

            # IF COUNT IS NOT 3 AND THE BOARD IS FULL THEN ITS A DRAW
            if self.is_Board_full():
                root = tkinter.Tk()
                ws = root.winfo_screenwidth() # width of the screen
                hs = root.winfo_screenheight() # height of the screen
                root.geometry('%dx%d+%d+%d' % (200, 200, (2*ws)//3, hs//2))
                tkinter.messagebox.showinfo('Alert', 'The game is draw...!!')
                root.destroy()
                self.game_over = self.is_Board_full()
                self.instructions()



    def design(self, surface):
        surface.blit(back, (0, 0)) # INSERTING THE BACKGROUND IMAGE

        for line in self.Board_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)


        # INSERTS THE LETTER AND X and O ACCORDING THE VALUE IN THE Board
        for y in range(len(self.Board)):
            for x in range(len(self.Board[y])):
                if self.get_cell_value(x, y) == "X":
                    surface.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x, y) == "O":
                    surface.blit(letterO, (x*200, y*200))



    def get_cell_value(self, x, y):
        return self.Board[y][x] # RETURNS THE Board VALUE AT GIVEN INDEX


    def set_cell_value(self, x, y, value):
        self.Board[y][x] = value  # SETS THE Board VALUE AT GIVEN INDEX


    def plotting_and_checking(self, x, y, player): # SETS THE Board VALUE AND CHECK FOR WINNING
        self.set_cell_value(x, y, player)
        self.check_Board(x, y, player)



    def is_possible(self, x, y): # DETERMINES IF THE CELL WE ARE SEARCHING FOR IS VALID
        return x >= 0 and x < 3 and y >= 0 and y < 3



    def is_Board_full(self): # CHECKING IF ALL THE CELLS ARE FILLED UP
        for row in self.Board:
            for value in row:
                if value == 0:
                    return False
        return True



    

    
    def clear_Board(self):
        for y in range(len(self.Board)):
            for x in range(len(self.Board[y])):
                self.set_cell_value(x, y, 0)



    def instructions(self):
        # CREATING THE DIALOG BOX FOR INSTRUCTIONS
        root = tkinter.Tk()
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        instructions = "These are the instructions:\n ==> Press SPACE to restart the game after someone wins\n==> Press ESC to exit :)"
        root.geometry('%dx%d+%d+%d' % (200, 200, ws//2, hs//2))
        tkinter.messagebox.showinfo('Instructions', instructions)
        root.destroy()







HOST = '192.168.1.9'
PORT = 65433

sock = socket.socket()
sock.connect((HOST, PORT))







def receive_data():
    global turn
    while True:
        data = sock.recv(1024).decode() # receive data from the server, it is a blocking method
        data = data.split('-') # the format of the data after splitting is: ['x', 'y', 'yourturn', 'playing']
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            Board.game_over = True
        if Board.get_cell_value(x, y) == 0:
            Board.plotting_and_checking(x, y, 'X')

# run the blocking functions in a separate thread
create_thread(receive_data)






# OBJECT OF Board CLASS
Board = Board()
Board.design(surface)
running = True
player = "O"
turn = False
playing = 'True'



# THE SENDING PART
while running:
    for event in pygame.event.get():  # THE EVENTS IN PYGAME ARE STORED IN A QUEUE AND ARE THEN IMPLEMENTED
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not Board.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not Board.game_over: # IF ITS YOUR TURN
                    pos = pygame.mouse.get_pos()
                    X, Y = pos[0] // 200, pos[1] // 200
                    if Board.get_cell_value(X, Y) == 0:
                        send_data = '{}-{}-{}-{}'.format(X, Y, 'yourturn', playing).encode()
                        sock.send(send_data)
                        Board.plotting_and_checking(X, Y, player)
                        if Board.game_over:
                            playing = 'False'
                        turn = False


        # HANDLING KEYBOARD INPUTS USING K_<KEY NAME>
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Board.game_over:
                Board.clear_Board()
                Board.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False


    Board.design(surface)
    pygame.display.flip()
