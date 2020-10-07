import socket
import threading
from _thread import start_new_thread

print_lock = threading.Lock()


def threaded(conn, addr):
    while True:
        data = conn.recv(1024)

        if not data:
            print("Connection lost", addr[0], addr[1])
            break
        conn.send(data)
    conn.close()


def main():
    host_id = ""
    port_id = 10001

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind((host_id, port_id))
    print("Server binded at", host_id, port_id)

    sock.listen(5)
    print("Server is working")

    while True:
        conn, addr = sock.accept()
        print("Connected to ", addr[0], addr[1])

        print_lock.acquire()
        start_new_thread(threaded, (conn, addr,))
        print_lock.release()

    sock.close()


if __name__ == "__main__":
    main()