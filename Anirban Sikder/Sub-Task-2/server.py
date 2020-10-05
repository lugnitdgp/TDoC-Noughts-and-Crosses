import socket
import threading
from _thread import start_new_thread

print_lock = threading.Lock()
all_connections = []
all_address = []

# Defining The Host and Port And Creating A Socket


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(msg)

# Binding The Socket With Port And Listening


def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(5)
    except:
        print("Could Not Bind To The Port " + str(port) + " Retrying...")
        bind_socket()


def accepting_connections():
    # Deleting And Closing All Existing Connection
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        conn, address = s.accept()
        s.setblocking(1)  # Prevent Time-Out
        all_connections.append(conn)
        all_address.append(address)
        print("Connection Has Been Established With ---- IP :" +
              address[0] + " Port : " + str(address[1]))
        start_new_thread(command, (conn, address))
    exit()


def command(conn, address):
    while True:
        data = conn.recv(1024)
        print("Message From Port : " +
              address[0] + " Port : " + str(address[1]) + " >>> ", end="")
        print(data.decode("utf-8"))
        if data == b'\x00':
            print("Bye !")
            conn.sendall(data)
            break
        conn.sendall(data)
    conn.close()


create_socket()
bind_socket()
accepting_connections()
