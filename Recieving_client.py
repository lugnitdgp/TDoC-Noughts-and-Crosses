import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = socket.gethostname()
port = 8001

sock.bind((ip, port))
print("Running on:", ip, port)

received_mesg = sock.recv(1024).decode('utf-8')

if received_mesg == "ping":
    sock.sendto(str("PONG").encode('utf-8'), (ip, 8000))
    print("Sending:", "PONG")