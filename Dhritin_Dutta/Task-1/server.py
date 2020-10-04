import socket
s = socket.socket()
s.bind(('', 12345))
s.listen()
c, addr = s.accept()
print("Connected to", addr)
c.send(str.encode("ping!Send '!quit' to quit"))
print(str(c.recv(1024), "utf-8"))
message1 = ''
while message1 != "!quit":
	message1 = input(">>")
	c.send(str.encode(message1))
	message2 = str(c.recv(1024), "utf-8")
	if message2 != "!quit":
		print(message2)
	else:
		break
s.close()       

