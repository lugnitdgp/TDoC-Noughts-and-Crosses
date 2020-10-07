import socket

def main():
    # server hostname and port to connect to
    host_id = ''
    port_id = 10001

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((host_id, port_id))

    mesg = "hello"
    while True:
        sock.send(mesg.encode('utf-8'))
        received_data = sock.recv(1024)

        print("Received data:", received_data.decode('utf-8'))
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break

    sock.close()

if __name__ == "__main__":
    main()