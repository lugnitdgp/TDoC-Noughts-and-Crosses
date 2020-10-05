import socket

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

# Accepting THe Connection


def accept_client():
    conn, address = s.accept()
    print("Connection Established --- IP : " +
          address[0] + " Port : " + str(address[1]))
    command(conn)
    conn.close()

# The Main Task Of Echo Goes Here


def command(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        conn.sendall(data)
        if data == b'\x00':
            break


def main():
    create_socket()
    bind_socket()
    accept_client()


main()
