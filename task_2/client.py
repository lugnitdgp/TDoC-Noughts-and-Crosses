import socket 
import threading
def threaded(c):
    while True:
        msg = str(input())
        print("you >> %s"%msg)
        c.sendall(str.encode(msg))
        data = c.recv(1024)
        recieve = data.decode('utf-8')
        print("server >> %s"%recieve)
        if data != '':
            continue
        else:
            print("your connection has been ended")
            break


if __name__ == "__main__":
    s = socket.socket()
    host = "192.168.137.1"
    port = 10000
    s.connect((host,port))
    t = threading.Thread(target=threaded,args=(s,))
    t.start()
