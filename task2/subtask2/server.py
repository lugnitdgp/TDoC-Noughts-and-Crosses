import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1233

try:
    s.bind((host, port))
    s.listen(5)
except socket.error:
    print("Not connected!")
thread_count = 0


def threaded(conn, addr):
    global thread_count
    conn.sendall(str.encode("Welcome! You are connected to the server!"))
    while True:
        try:
            data = conn.recv(1024)
        except socket.error:
            break
        if data.decode("utf-8") == 'quit':
            conn.close()
            print(f"Closed connection for {addr[0]} {addr[1]}")
            thread_count-=1
        else:
            print("'"+ data.decode('utf-8') + "' from the client at " + addr[0] + " " + str(addr[1]) + "")


while True:
    conn, addr = s.accept()
    thread_count +=1
    print("connected to "+addr[0]+" and "+str(addr[1])+"")
    print("Total number of thread is : ", thread_count)
    if thread_count == 0:
        break
    start_new_thread(threaded, (conn,addr))


