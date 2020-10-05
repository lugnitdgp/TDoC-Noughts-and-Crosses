# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 

print_lock = threading.Lock() 

# thread function 
def threaded(conn): 
	while True: 

		# data received from client 
		data = conn.recv(1024)
		if not data: 
			print("Bye") 

			# lock released on exit 
			print_lock.release() 
			break
		print("from connected user: " + str(data))

		conn.send(data)

	# connection closed 
	conn.close() 


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

		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', address[0], ':', address[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (conn,)) 
	sock.close() 


if __name__ == '__main__': 
	main() 
