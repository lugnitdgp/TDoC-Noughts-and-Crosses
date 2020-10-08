#! /usr/bin/python3

import socket

HOST = ''
PORT = 9989
SERVER = None
BUFF_SIZE = 1024

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
        SERVER.listen(1)
        print("SERVER listening for connections...")
    except:
        print("Socket Binding Error!!")

def accept_connections():
    global SERVER
    while True:
        connection, address = SERVER.accept()
        print("[NEW Connection] Connection established with {} on port {}".format(address[0], address[1]))
        handle_client(connection, address)

def handle_client(conn, addr):
    incoming_msg = conn.recv(BUFF_SIZE)
    incoming_msg = incoming_msg.decode('utf-8')
    
    if incoming_msg is not '':
        conn.send(bytes('Congrats!! You are now connected to the server...\nYou sent : ' + incoming_msg, 'utf-8'))
        print(f'Message from Client {addr[0]}:{addr[1]} > ', incoming_msg)        
        while True:
            incoming_msg = conn.recv(BUFF_SIZE)
            incoming_msg = incoming_msg.decode('utf-8')
            if incoming_msg is '':                
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
