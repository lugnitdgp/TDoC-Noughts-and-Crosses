import socket
import sys
from _thread import *
import threading

thread_lock = threading.Lock()
thread_count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

host = '127.0.0.1'
port = 1234

s.bind((host, port))
print('socket bound to ' + str(host) + ': ' + str(port))

s.listen(5)
print('listening')


def threaded_client(connection, adr):
    connection.sendall(b'Welcome to the server')
    print('connected to ', address)

    while True:
        data = connection.recv(1024).decode('utf-8')
        if data == '' or data == 'quit':
            print('Thread ', adr, 'closed')
            break

        print(adr, ' says ' + str(data))

    connection.close()
    global thread_count
    thread_count -= 1


while True:
    con, address = s.accept()
    thread_count += 1
    thread_lock.acquire()
    start_new_thread(threaded_client, (con, address))

    print("No. of active threads connected: " + str(thread_count))
    thread_lock.release()
