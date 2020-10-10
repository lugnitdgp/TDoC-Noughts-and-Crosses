import socket
import sys
import uuid
import threading

class Client:
    def __init__(self, ADDR, DISCON_MSG='QUIT'):
        try:
            self.ID = uuid.uuid1()
            self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.DISCON_MSG = DISCON_MSG
            self.ADDR = ADDR
            self.SOCK.connect(ADDR)
            print(f'[CONNECTION SUCCESS] Connected to server {ADDR} ...')
        except:
            print('[SOMETHING WENT WRONG]...')
            sys.exit(0)
        

    def send_message(self, message, FORMAT='utf-8'):
        self.SOCK.sendall(bytes(message, FORMAT))
        if message == self.DISCON_MSG:
            print("[CONNECTION CLOSED]")
            self.SOCK.close()
            sys.exit(0)
        
    def recv_resp(self, CHUNKS=1024, FORMAT='utf-8'):
        data = self.SOCK.recv(CHUNKS).decode(FORMAT)
        if data=='FULL SHUTDOWN':
            sys.exit(0)
        print(f'\b\b[RESPONSE FROM {self.ADDR}] : {data}\n> ', end="")
        return data

    def assign_room(self, room_id):
        self.ROOM = room_id

    def send_creds(self):
        data = '{}#{}'.format(self.ROOM, self.ID).encode()
        self.SOCK.send(data)


def cl_listen(client):
    try:
        while client.SOCK:
            client.recv_resp()
    except:
        return

HOST = socket.gethostname()
PORT = 3034 # change this to the port client1 is running
ADDR = (HOST, PORT)

client = Client(ADDR, 'Quit')
roomId = input('[ENTER ROOM ID]: ')
client.assign_room(roomId)

# sending room id and uuid of the client 
client.send_creds()
t = threading.Thread(target=cl_listen, args=[client])
# t.daemon=True
t.start()
while client.SOCK:
    data = input('> ')
    client.send_message(data)
    # client.recv_resp()
    