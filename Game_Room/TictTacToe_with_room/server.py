import socket
import sys
import threading

class ClientObj:
    def __init__(self, sock, addr, room, iid):
        self.ROOM = room
        self.SOCK = sock
        self.ADDR = addr
        self.ID= iid

class Server:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        self.ROOMS = {}
        self.ADDR = ADDR
        self.DISCON_MSG = DISCON_MSG
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def create_rooms(self, client):
        if client.ROOM in self.ROOMS.keys():
            if len(self.ROOMS[client.ROOM])>=2 :
                self.send_resp(client.SOCK, 'FAILURE')
            else:
                self.ROOMS[client.ROOM].append(client)
                self.send_resp(client.SOCK, '2')
        else:
            self.ROOMS[client.ROOM] = [client]
            self.send_resp(client.SOCK, '1')

    def init(self):
        self.SOCK.bind(self.ADDR)
        print(f'[SERVER STARTED] at {self.ADDR}...')
        self.SOCK.listen()
        return self.SOCK

    def accept_client(self):
        conn, addr = self.SOCK.accept()
        print(f'[NEW CONNECTION] Client {addr} added...')
        return conn, addr

    def recv_message(self, conn, addr, CHUNKS=1024, FORMAT='utf-8'):
        data = conn.recv(CHUNKS).decode(FORMAT)
        print(f'[MESSAGE FROM] : \t{data}')
        return data
        
    def send_resp(self, conn, RESPONSE, FORMAT='utf-8'):
        print(f'[RESPONSE GIVEN by {self.ADDR}] : \t{RESPONSE}')
        conn.send(bytes(RESPONSE, FORMAT))

    def handle_client(self, client):
        while True:
            client_msg = self.recv_message(client.SOCK, client.ADDR)
            if client_msg == self.DISCON_MSG:
                print(f'[CLIENT LEFT] Client {client.ADDR} left server')
                break

            for obj in self.ROOMS[client.ROOM]:
                if obj.ID != client.ID:
                    self.send_resp(obj.SOCK, client_msg)

            print('[MESSAGE SENT]')
    
        try:
            client.SOCK.close()
            for index, obj in enumerate(self.ROOMS[client.ROOM]):
                if obj.ID == client.ID:
                    del self.ROOMS[client.ROOM][index]
                    return
            return
        except:
            print('HANDLING CLIENT ERROR')
            return
            


HOST = socket.gethostname()
PORT = 3034 # change this to any other available port
ADDR = (HOST, PORT)
ROOMS = {}
server = Server(ADDR, 'Quit')
server_sock = server.init()

while server_sock:
    conn, addr = server.accept_client()
    creds = server.recv_message(conn, addr)
    tempClient = ClientObj(conn, addr, creds.split('#')[0], creds.split('#')[1])
    server.create_rooms(tempClient)
    t = threading.Thread(target=server.handle_client, args=[tempClient])
    t.start()
    print(f'[ACTIVE CLIENTS] {threading.activeCount()-1}') 
    # reason of subtracting 1 is this loop is also a thread, so to get all the connections we have to subtract 1
    
