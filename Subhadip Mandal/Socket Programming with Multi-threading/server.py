import socket
import threading

host = "127.0.0.1"
port = 9997
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


def handle_client(sock):
    sock.listen(1)
    conn, addr = sock.accept()
    print(f'Connection established. | IP: {addr[0]} | Port: {addr[1]}')
    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        else:
            conn.send(msg)


threads = []

# change the range as per number of clients.
for _ in range(2):
    t = threading.Thread(target=handle_client, args=[s])
    t.daemon = True
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
