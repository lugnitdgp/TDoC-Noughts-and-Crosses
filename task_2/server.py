import socket
import threading 
def threaded(c):
    while True:
        msg = c.recv(1024)
        data = msg.decode('utf-8')
        print(data)
        if msg =='':
            print("client ended connection")
            c.send(str.encode("you connection ended"))
            break
        else:
            c.send('you are connected')
    c.close()
    
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = ""
    port = 10000
    s.bind((host,port))
    s.listen(10)
    conn, addr = s.accept()
    t = threading.Thread(target=threaded,args=(conn,))
    t.start()
