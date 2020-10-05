# IT IS THE SERVER FILE SO PLEASE RUN IT FIRST
# NOTE THE SERVER FILE WILL RUN ALWAYS TILL IT IS TERMINATED EXPLICITLY

import socket
import sys
from _thread import *
import threading
ThreadCount = 0
print_lock = threading.Lock()



'''
THE THREADING LOCK IS QUITE AWESOME IN THE SENSE THAT:
SUPPOSE A FUNCTION HAS BEEN COMMUNICATING IN A THREAD AND IF YOU HAVE APPLIED THE 
THREAD LOCK IN IT USING .acquire() FUNCTION THEN THE THREAD BECOMES LOCKED AND ALL THE CONNECTION
WILL BE GOING ON THAT THREAD ITSELF AND NO OTHER THREAD WILL INTERFERE IN BETWEEN

WHEN YOU RELEASE THE LOCK USING .release() FUNCTION THEN ONLY THE THREAD WILL BE LEFT AND OTHER THREADS CAN COMMUNICATE TOO. 

IF YOU DO NOT USE THREAD...THEN ALL THE THREADS CAN WORK INDEPENDENTLY... :)

'''



# CREATING SOCKET 
def create_socket():
    try:
        global host
        global port
        global s
        host = ""  
        port = 9999 # Port to listen on (non-privileged ports are > 1023)

        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error:", msg)


# BINDING THE PORT WITH SOCKET AND LISTENING FOR CONNECTION
def binding_socket():
    global host
    global port
    global s

    print("Binding the port:", port)

    try:
        s.bind((host,port))
        s.listen(1) # It has a backlog parameter. Specify the number of connections to allow simulatneously

    except socket.error as msg:
        print('socket binding error:', msg)
        print('retrying...')

        binding_socket() # if the socket fails to bind or listen, then retry...


# ACCEPTING FROM CLIENT
def socket_accept():
    global ThreadCount
    while True:
        connection, address = s.accept()  # connection is a socket object that has various functions to execute
        # system calls like send(), recv()

        print("Connection has been established! | IP", address[0], ' | PORT', address[1])

        start_new_thread(communicating_with_client,(connection, address))
        ThreadCount += 1
        print('Thread Number: ', ThreadCount)


def communicating_with_client(connection, address):
    #print_lock.acquire()
    while True:
        data = str(connection.recv(2048), 'utf-8')


        # BREAKING THE CONNECTION IF EMPTY STRING IS PASSED
        if data == '':
            print('breaking up with: ', address[0], 'Port: ', address[1])

        # print_lock.release()
            break


        print('IP: ', address[0],'Port: ',address[1],'saying===> ',data)
        

        message = 'I have printed: ' + data
        connection.send(str.encode(message)) #sending feedback back to client

    connection.close()



def main():
    create_socket()
    binding_socket()
    socket_accept()

main()
