# IT IS THE SERVER FILE SO PLEASE RUN IT FIRST


import socket


# CREATING SOCKET 
def create_socket():
    try:
        global host
        global port
        global s
        host = ""  # Standard interface address (localhost)
        port = 9998 # Port to listen on (non-privileged ports are > 1023)

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
        s.listen(5) # It has a backlog parameter. Specify the number of connections to allow simulatneously

    except socket.error as msg:
        print('socket binding error:', msg)
        print('retrying...')

        binding_socket() # if the socket fails to bind or listen, then retry...


# ACCEPTING FROM CLIENT
def socket_accept():
    connection, address = s.accept()  # connection is a socket object that has various functions to execute
    # system calls like send(), recv()

    print("Connection has been established! | IP", address[0], ' | PORT', address[1])
    send_commands(connection)
    connection.close()


# RECEIVING FROM AND SENDING TO CLIENT
def send_commands(connection):
    while True:
        data = str(connection.recv(1024), 'utf-8') # receiving from client
        

        if data == '':
            print('Breaking the connection...')
            s.close()
            break
            


        print("Received: ", data)

        message = 'I have printed: ' + data + '...'
        connection.send(str.encode(message)) # sending feedback to client
        




def main():
    create_socket()
    binding_socket()
    socket_accept()

main() 