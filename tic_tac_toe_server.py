import socket
import re

# initialize the game board
def init_game(csocket):

	board = [' ' for x in range(10)] #list to contain player's moves
	print("I will start the game")
	print_board(board)	# to print the intialized board
	print("Type q when you want to quit")
	start_game(csocket, board)	#start the game


# to start the game 
def start_game(csocket, board):
	
	#while the board is not full
	while not isBoardFull(board):
		print("Your turn")
		#get move from the server
		server_move = input("Enter a number between 1 to 9 to mark your position in the grid \n > ")
		#check if its not a quit message
		if(str(server_move) == 'q'):
			server_quit = "Server has quit the game..Byee"
			print("Thanks for playing")
			csocket.send(bytes(server_quit, 'utf-8'))
			break
		#change the input to int type
		server_move = int(server_move)
		#while the input is invalid, get input from the server again
		while not checkMoveIsValid(board, server_move):
			server_move = int(input("Invalid....Enter your position in the grid (1-9)  : "))

		#update board if the move is valid
		board[server_move] = 'X'
		#print the board
		print_board(board)

		#if the board is full, but X is not the winner, then the match is draw
		if (isBoardFull(board) and  not checkWinner(board, 'X')):
			match_draw = "Game Draw!!!! Until next time"
			print(match_draw)
			csocket.send(bytes(match_draw, 'utf-8'))
			csocket.send(bytes(str(server_move), 'utf-8'))
			break

		#check if server wins
		if checkWinner(board, 'X'):
			print("Server wins this time")
			server_win = "Server Won!!! You lose... Good luck next time :) "
			csocket.send(bytes(server_win, 'utf-8'))
			csocket.send(bytes(str(server_move), 'utf-8'))
			break

		#If the server has not won yet and the board is not full
		else:
			#send the server's move to the client
			csocket.send(bytes(str(server_move), 'utf-8'))
			#wait for the client to play
			print("Wait for the client to playy ...")
			#get the client's move
			client_move = csocket.recv(1024).decode('utf-8')
			#if the client has sent a quit message, then break out of the loop
			if(re.search("quit the game", client_move)):
				print(client_move)
				break
			#else, conver the client's move to integer type
			else:
				client_move = int(client_move)
		
		#update the board with client's move
		board[client_move] = 'O'

		#check if the board is full and the client has not won, then the match is draw
		if (isBoardFull(board) and  not checkWinner(board, 'O')):
			match_draw = "Game Draw!!!! Until next time"
			print(match_draw)
			csocket.send(bytes(match_draw, 'utf-8'))
			break

		#if the client has won, send the winning message to client
		if checkWinner(board, 'O'):
			print("Client's Move: ", client_move)
			print_board(board)	#print the board
			print("Client wins this time")
			client_win = "Congratulations...You Won!!! See you next time :) "
			csocket.send(bytes(client_win, 'utf-8'))
			break

		#If the client has not won yet and the board is not full, continue the game
		else:
			print("Client's Move: ", client_move)
			print_board(board)
			

#Function to check if 'X' or 'O' has won the game
def checkWinner(board, letter):
	return ((board[1] == letter and board[2] == letter and board[3] == letter) or #across top
			(board[4] == letter and board[5] == letter and board[6] == letter) or #across middle
			(board[7] == letter and board[8] == letter and board[9] == letter) or #across bottom
			(board[1] == letter and board[4] == letter and board[7] == letter) or #down left
			(board[2] == letter and board[5] == letter and board[8] == letter) or #down middle
			(board[3] == letter and board[6] == letter and board[9] == letter) or #down right
			(board[1] == letter and board[5] == letter and board[9] == letter) or #diagonal right
			(board[3] == letter and board[5] == letter and board[7] == letter)) #diagonal left

#Function to check if the move is valid
def checkMoveIsValid(board, move):
	#if the number is invalid
	if move < 1 or move > 9:
		return False
	#if the move is already taken
	if board[move] == 'O' or board[move] == 'X': 
		return False
	else:
		return True

#function to check if the board is full
def isBoardFull(board):
	#If the board has empty spaces, return False
	if board.count(' ') > 1:
		return False
	#else, return true
	else:
		return True

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

#function to start the chat with the client
def client_chat(server_socket):

	#Server accepts the connection from the client
	csocket, client_address = server_socket.accept()
	print("Connected by ", str(client_address))

	welcome = "Welcome to the game. Do you want to start the game? Send yes if you want to start or no if you want to quit \n (yes, no)"
	csocket.send(bytes(welcome, 'utf-8'))

	msg_recv = ""
	msg_recv = csocket.recv(1024).decode('utf-8')
	
	#if the client accepts to play the game, initialize the game
	if(re.search("yes",msg_recv)):
		init_game(csocket)

	#else, send goodbye message
	else:
		goodbye_msg = "Okay..Take care..See you next time"
		print("Client rejected the game request..Goodbye")
		csocket.send(bytes(goodbye_msg, 'utf-8'))
		return
        
#Main Function
def main():
	#Host and port for binding to the server
	host = socket.gethostbyname("localhost")
	port = 12345

	#set up socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#To overcome the address already in use message to modify the socket to reuse the address
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#Bind the host and port with the server
	server_socket.bind((host, port))
	#Listen for connection
	server_socket.listen(5)
	print("Server listening on : ", host, "on port: ", port)

	#call for chat function
	client_chat(server_socket)
	
	#Once the function is returned, close the socket connection
	server_socket.close()

#Call for main function
if __name__ == '__main__':
	main()