import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = socket.gethostname()
port = 8000

sock.bind((ip, port))
print("Running on:", ip, port)

mesg = "PING"
print("Sending", mesg)

sock.sendto(str(mesg).encode('utf-8'),(ip,8001))
received_mesg = sock.recv(1024).decode('utf-8')

print("Received", received_mesg)