import socket
HOST = "127.0.0.1"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(bytes("This is from Client",'UTF-8'))
while True:
  data =  s.recv(1024)
  print("From Server :" ,data.decode())
  sendd = input()
  s.sendall(bytes(sendd,'UTF-8'))
  if sendd=='bye':
      break
s.close()