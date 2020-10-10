#! /usr/bin/python3

import socket
import threading

HOST = socket.gethostname()
PORT = 9989
SERVER = None
BUFF_SIZE = 1024
THREAD_LOCK = threading.Lock()
CLIENT_CONNECTIONS = None
CONNECTED_TO = None

def create_server():
    global SERVER
    try:
        SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("SERVER created successfully")
    except Exception as e:
        print("Socket Creation Error!!\n", e)
        exit()

def bind_server_and_listen():
    global SERVER, HOST, PORT, CLIENT_CONNECTIONS, CONNECTED_TO
    try:
        SERVER.bind((HOST, PORT))
        SERVER.listen(5)
        CLIENT_CONNECTIONS = []
        CONNECTED_TO = []
        print("SERVER listening for connections...")
    except Exception as e:
        print("Socket Binding Error!!\n", e)
        exit()

def accept_connections():
    global SERVER, CLIENT_CONNECTIONS
    while True:
        connection, address = SERVER.accept()
        print("[NEW Connection] Connection established with {} on port {}".format(address[0], address[1]))
        THREAD_LOCK.acquire()
        CLIENT_CONNECTIONS.append(connection)
        CONNECTED_TO.append(-1)
        threading.Thread(target=handle_client, args=(connection, address)).start()
        THREAD_LOCK.release()

def handle_client(conn, addr):
    incoming_msg = conn.recv(BUFF_SIZE)
    incoming_msg = incoming_msg.decode('utf-8')
    self_index = CLIENT_CONNECTIONS.index(conn)
    peer_index = -1
    peer_conn = None
    connected_to_peer = False

    if incoming_msg == 'CONNECT':        
        while True:
            THREAD_LOCK.acquire()
            if not connected_to_peer:
                if CONNECTED_TO[self_index] == -1:                
                    try:                        
                        peer_index = CONNECTED_TO.index(-1)
                        if peer_index == self_index:
                            peer_index = CONNECTED_TO.index(-1, self_index+1)
                        try:
                            conn.send(bytes('You are player X', 'utf-8'))
                        except ConnectionResetError:
                            break                        
                        CONNECTED_TO[self_index] = peer_index
                        CONNECTED_TO[peer_index] = self_index
                        peer_conn = CLIENT_CONNECTIONS[peer_index]
                        connected_to_peer = True
                        
                        peer_conn.send(bytes('You are player O', 'utf-8'))
                    except ValueError:
                        THREAD_LOCK.release()
                        continue
                else:
                    peer_index = CONNECTED_TO[self_index]
                    peer_conn = CLIENT_CONNECTIONS[peer_index]
                    connected_to_peer = True
            THREAD_LOCK.release()
            try:
                self_move = conn.recv(BUFF_SIZE)
            except ConnectionResetError:
                try:
                    peer_conn.send(bytes('QUIT', 'utf-8'))
                except OSError:
                    pass
                break
            if not self_move:
                try:
                    peer_conn.send(bytes('QUIT', 'utf-8'))
                except OSError:
                    pass
                break
            elif self_move.decode('utf-8') == '[GAME OVER]':
                peer_conn.send(self_move)
                self_move = conn.recv(BUFF_SIZE)
                peer_conn.send(self_move)
                break
            else:
                peer_conn.send(self_move)

    THREAD_LOCK.acquire()
    try:
        self_index = CLIENT_CONNECTIONS.index(conn)
        del CLIENT_CONNECTIONS[self_index]
        del CONNECTED_TO[self_index]
        peer_index = CLIENT_CONNECTIONS.index(peer_conn)
        del CLIENT_CONNECTIONS[peer_index]
        del CONNECTED_TO[peer_index]
    except ValueError:
        pass
    THREAD_LOCK.release()

    conn.close()
    print(f"[Closed Connection] Connection closed for {addr[0]} on port {addr[1]}")

if __name__ == '__main__':
    create_server()
    bind_server_and_listen()
    accept_connections()
    SERVER.close()
