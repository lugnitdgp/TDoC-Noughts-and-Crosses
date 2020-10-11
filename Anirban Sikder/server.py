import socket, threading

# Number Of Connections
count = 0

def accept_client():
    global count
    while True:
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024).decode()
        CONNECTION_LIST.append((uname, cli_sock))
        print('%s is now connected' %uname)
        count += 1
        thread_client = threading.Thread(target = broadcast_usr, args=[uname, cli_sock])
        thread_client.start()

def broadcast_usr(uname, cli_sock):
    global count
    while True:
        data = cli_sock.recv(1024).decode()
        if(data=='quit'):
            print("{0} disconnected".format(uname))
            count -= 1
            if(count == 0):
                cli_sock.close()
                exit()
            cli_sock.close()
            break
        elif data:
            print ("{0} spoke : ".format(uname) , end="")
            print (data)
            b_usr(cli_sock, uname, data)


def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if (client[1] != cs_sock):
            client[1].send(sen_name.encode("utf-8"))
            client[1].send(msg.encode("utf-8"))

if __name__ == "__main__":    
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(5)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()