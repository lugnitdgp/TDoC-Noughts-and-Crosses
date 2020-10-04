#! /usr/bin/python3

import socket
import threading

HOST = ''
PORT = 9989
SERVER = None
BUFF_SIZE = 1024
THREAD_LOCK = threading.Lock()

def create_server():
    global SERVER
    try:
        SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("SERVER created successfully")
    except:
        print("Socket Creation Error!!")

def bind_server_and_listen():
    global SERVER
    try:
        SERVER.bind((socket.gethostname(), PORT))
        SERVER.listen(5)
        print("SERVER listening for connections...")
    except:
        print("Socket Binding Error!!")
        #bind_server_and_listen()

def accept_connections():
    global SERVER
    while True:
        connection, address = SERVER.accept()
        print("[NEW Connection] Connection established with {} on port {}".format(address[0], address[1]))
        threading.Thread(target=handle_client, args=(connection, address)).start()

def handle_client(conn, addr):
    incoming_msg = conn.recv(BUFF_SIZE)
    incoming_msg = incoming_msg.decode('utf-8')
    
    if incoming_msg is not '':
        conn.send(bytes('Congrats!! You are now connected to the server...\nYou sent : ' + incoming_msg, 'utf-8'))
        print(f'Message from Client {addr[0]}:{addr[1]} > ', incoming_msg)
        THREAD_LOCK.acquire()
        while True:
            incoming_msg = conn.recv(BUFF_SIZE)
            incoming_msg = incoming_msg.decode('utf-8')
            if incoming_msg is '':
                THREAD_LOCK.release()
                break
            else:
                conn.send(bytes('You sent : ' + incoming_msg, 'utf-8'))
                print(f'Message from Client {addr[0]}:{addr[1]} > ', incoming_msg)

    conn.close()
    print(f"[Closed Connection] Connection closed for {addr[0]} on port {addr[1]}")

if __name__ == '__main__':
    create_server()
    bind_server_and_listen()
    accept_connections()
