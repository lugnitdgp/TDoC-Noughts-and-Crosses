import socket
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Done!")
print(str(s.recv(1024), "utf-8"))
s.send(str.encode("Pong! Send '!quit' to close connection."))
message1 = ''
while message1 != "!quit":
	message2 = str(s.recv(1024), "utf-8")
	if message2 != "!quit":
		print(message2)
	else:
		break
	message1 = input(">>")
	s.send(str.encode(message1))
s.close()
