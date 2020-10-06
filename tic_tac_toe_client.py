import socket
import sys 
import re

#function to initialize the game board
def init_game(csocket):
    board = [' ' for x in range(10)]
    print("Server will start the game")
    print_board(board)
    #start the game
    start_game(csocket, board)

#function to start the game
def start_game(csocket, board):
    
    while True:
        
        #get the server's move
        server_move = csocket.recv(1024).decode('utf-8')

        #if the server's move is either a server's winning msg or draw msg
        if(re.search("Server Won", server_move) or re.search("Game Draw", server_move)):
            final_move = csocket.recv(1024).decode('utf-8')
            board[int(final_move)] = 'X'
            print("Server's move: ", str(final_move))
            print_board(board)
            print(server_move)
            break
        
        #if the server's move is quitting the game
        elif(re.search("quit the game", server_move)):
            print(server_move)
            break

        #if the server's move is client's winning message
        elif(re.search("You Won", server_move)):
            print(server_move)
            break
        #if the server's move is an actual move in the game board
        else:
            server_move = int(server_move)
            #update board
            print("Server's Move: ", server_move)
            board[server_move] = 'X'
            #print board
            print_board(board)

            #get the move from client
            print("Your turn")
            client_move = input("Enter your position in the grid (1-9) \n > ")
            
            #check if the client's msg is a quit msg
            if(str(client_move) == '/q'):
                client_quit = "Client has quit the game..Byee"
                print("Thanks for playing")
                csocket.send(bytes(client_quit, 'utf-8'))
                break
            
            else:
                #convert the client_move's type to int
                client_move = int(client_move)
                #check if the client's move is valid
                while (client_move < 1 or client_move > 9 or board[client_move] != ' '):
                    client_move = int(input("Invalid!!Enter your position in the grid \n > "))

                #if valid, update the board and print it
                board[client_move] = 'O'
                print_board(board)
                #send the client's move to server
                csocket.send(bytes(str(client_move), 'utf-8'))
                print("Wait for the server to play...")


#function to print the game board
def print_board(board):
    print('******************')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('******************')

#function which handles the server client chat in the client side of the project
def server_chat(csocket):
    
    msg_recv = csocket.recv(1024).decode('utf-8')
    print(msg_recv)
    #prompt for the message to be sent to the server 
    msg_to_send = input(">")
    
    #send the message by converting into bytes to the server
    csocket.send(bytes(msg_to_send, 'utf-8'))

    #if the client wants to continue, intiate the game
    if(re.search("yes", msg_to_send)):
        print("Type /q when you want to quit")
        init_game(csocket)
    #if the client doesnt want to continue, send quit msg
    else:
        msg_recv = csocket.recv(1024).decode('utf-8')
        print(msg_recv)
        return
        

#main function       
def main():

    #host and port for connecting the socket
    host = socket.gethostbyname("localhost")
    port = 12345

    #set up a socket
    csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect the socket with the host and port
    csocket.connect((host, port))
    print("Connected to: ", host, "on port:", port)

    #start the chat with the server
    server_chat(csocket)
    #After chatting is exited, close the socket
    csocket.close()

#call for main function
if __name__ == '__main__':
    main()