#! /usr/bin/python3

import time
import socket

HOST = socket.gethostname() 
PORT = 9989
CLIENT = None
BUFF_SIZE = 1024

def create_client():
    global CLIENT
    try:
        CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CLIENT.connect((HOST, PORT))
    except:
        print("Connection Error!!  Retrying...")
        time.sleep(2)
        create_client()

def communicate():
    global CLIENT
    while True:
        outgoing_msg = input('Type "PING" to get a response> ')
        CLIENT.send(bytes(outgoing_msg, 'utf-8'))
        if outgoing_msg == 'QUIT':
            break
        incoming_msg = CLIENT.recv(BUFF_SIZE)
        print(incoming_msg.decode('utf-8'))


if __name__ == '__main__':
    create_client()
    communicate()
