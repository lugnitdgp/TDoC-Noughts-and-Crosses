import socket

# creates a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 5051
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + msg)


# Binding the socket an listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error :" + msg + "n" + "Retrying...")
        bind_socket()


# Establish connection with a client(socket must be listening)

def socket_accept():
    global s1
    global host1
    global port1

    s1 = socket.socket()
    host1 = socket.gethostname()
    port1 = 5050

    s1.connect((host1, port1))
    conn, address = s.accept()
    print("Connection has been established |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)


# send commands to client
def send_commands(conn):
    while True:
        client_response = str(s1.recv(1024), "utf-8")
        # THE PING PONG
        if client_response != "PING":
            print(client_response)
        else:
            print("PONG")
        if client_response == "Quit!":
            conn.close()
            s.close()
            break
        txt = input()
        if txt == "quit":
            conn.send(str.encode("Quit!"))
            conn.close()
            s.close()
            break
        if len(str.encode(txt)) > 0:
            conn.send(str.encode(txt))


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()