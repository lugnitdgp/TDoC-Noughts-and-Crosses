import socket
import sys

host = ""
port = 9999

s = socket.socket()
s.bind((host, port))
s.listen(5)

conn, address = s.accept()
print("Connection Established With ----- Ip : " +
      address[0] + " Port : " + str(port))

conn.send(str.encode("Hurray , We Are Connected Now !!", "utf-8"))

print("[Type Quit To Exit !]")
print("Initiate The Chat (eg :- PING ): ")

while True:
    print("Client1>>> ", end="")
    msg = input()
    msg = "Client1>>> " + msg
    conn.send(str.encode(msg, "utf-8"))
    if(msg.lower() == 'client1>>> quit'):
        conn.close()
        break
    response = conn.recv(1024)
    response = response.decode("utf-8")
    if(response.lower() == 'client2>>> quit'):
        conn.close()
        break
    print(response)
