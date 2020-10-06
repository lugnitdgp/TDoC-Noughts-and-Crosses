# import socket programming library 
import socket 
import ttg
# import thread module 
from _thread import *
import threading 

print_lock = threading.Lock() 

# thread function 
def threaded(conn): 
	print("Player 1")

	while True: 
		p1 = input("-> ")  # take input
		ret = ttg.game(int(p1),1)

		while(ret == 1):	
			print("Choose again!!..")
			p1 = input("-> ")	
			ret = ttg.game(int(p1),1)
		if(int(p1) == 0 or ret == -1):
			print("Bye") 
			p2 = conn.recv(1024).decode('utf-8')
			# lock released on exit 
			print_lock.release() 
			conn.send(("0").encode('utf-8'))
			break
			# data received from client 
		p2 = conn.recv(1024).decode('utf-8')
		ret2 = ttg.game(int(p2),0)

		if(ret == 1):
			conn.send(("repeat").encode('utf-8'))
			ret2 = ttg.game(int(p2),0)
			while(ret2 == 1):
				p2 = conn.recv(1024).decode('utf-8')
				conn.send(("repeat").encode('utf-8'))
				ret2 = ttg.game(int(p2),0)
		if (int(p2) == 0 or ret2 == -1): 
			print("Bye........") 
			# lock released on exit 
			print_lock.release() 
			conn.send(("0").encode('utf-8'))
			break
		conn.send((" ").encode('utf-8'))
	conn.close() 
	print("out...")
		# print("from connected user: " + str(p2))	
	# connection closed 
	


def main(): 
	host = socket.gethostname()

	# reverse a port on your computer 
	# in our case it is 5000 but it 
	# can be anything 
	port = 8000
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	sock.bind((host, port)) 
	print("socket binded to port", port) 

	# put the socket into listening mode 
	sock.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		conn, address = sock.accept() 
		ttg.ini()
		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', address[0], ':', address[1]) 
		# Start a new thread and return its identifier 
		start_new_thread(threaded, (conn,)) 
	sock.close() 


if __name__ == '__main__': 
	main() 
