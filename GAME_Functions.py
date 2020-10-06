import socket

class Game_Rules():
    def __init__(self,type,socket,to_addr):
        self.marks={0:'O',1:'X'}
        self.board=[ ' ' for x in range(1,11)]
        #self.board={1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}
        self.gamesocket=socket
        self.to_addr=to_addr
        if type=="Server":
            self.instructions("X")
            self.server_loop()
        elif type=="Client":
            self.instructions("O")
            self.client_loop()
            
    def draw_board(self):
        for i in range(1,10):
            if i%3==0:
                if self.board[i]!=' ':
                    print(str(self.marks[self.board[i]])+' |')
                else:
                    print(' '+' |')
                    
                print("-----------")
            
            else:
                if self.board[i]!=' ':
                    print(str(self.marks[self.board[i]]),end=' | ')
                else:
                    print(' ',end=' | ')
                    
                
            
                
                

    def instructions(self,player):
        print("Welcome :)\nYou are Player:"+"'"+str(self.marks[player])+"'")
        print("To make a Move enter a number between 1-9")
        # grid is printed with position of each 
        for i in range(1,10):
            if i%3==0:
                print(str(i)+' |')
                print("-----------")
            
            else:
                print(i,end=' | ')
                
    def your_move(self,player):
        self.check_status()
        # 'position' stores the cell number on board for next move   
        position=int(input("Enter next move : "))
        while True:
            #if the position chosen by player is empty then the move is executed
            if self.board[position]==' ':
                self.board[position]=player
                self.gamesocket.sendto(str(position).encode('utf-8'),self.to_addr)
                break
            else:
                print("Enter a valid move")
        self.draw_board()
        self.check_status()

    def opponent_move(self,player):
        print("Waiting for the other player to move")
        position,_=self.gamesocket.recvfrom(1024)
        position=position.decode('utf-8')
        self.board[int(position)]=player
        self.draw_board()

    def server_loop(self):

        while True:
            self.opponent_move(player=0)
            self.your_move(player=1)

    def client_loop(self):

        while True:
            self.your_move(player=1)
            self.opponent_move(player=0)

    def check_status(self):
        symbol=' '
        b = self.board
        
        if (b[1] != ' ' and b[1] == b[2] and b[1] == b[3]): #row-1
            symbol=b[1]
            
        elif (b[4] != ' ' and b[4] == b[5] and b[4] == b[6]):#row -2 
            symbol=b[4]
            
        elif (b[7] != ' ' and b[7] == b[8] and b[7] == b[9]):#row - 3
            symbol=b[7]
            
        elif (b[1] != ' ' and b[1] == b[4] and b[1] == b[7]):#col 1
            symbol=b[1]
            
        elif (b[2] != ' ' and b[2] == b[5] and b[2] == b[8]):#col 2
            symbol=b[2]
            
        elif (b[3] != ' ' and b[3] == b[6] and b[3] == b[9]): #col 3
            symbol=b[3]
            
        elif (b[1] != ' ' and b[1] == b[5] and b[1] == b[9]): #diagonal 1
            symbol=b[1]
            
        elif (b[3] != ' ' and b[3] == b[5] and b[3] == b[7]):#diagonal 2
            symbol=b[1]

        if symbol!=' ':
            
            print("Winner is : ",self.marks[symbol])
            print("Game ends...")
            exit(0)
            
        
            
                                       
            
        
        
            
