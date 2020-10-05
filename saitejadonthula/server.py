
import socket
import threading

def client(c):
    try:
        conn.send(str.encode('connection is established...'))
        while True:
            msg=c.recv(1024)
            if msg=='':
                c.close()
                #pnt_lk.release()
                break
            c.send(msg)
    except :
        print('connection lost')

#pnt_lk = threading.Lock()
host = ""
port = 10000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
while True:
    conn,add= s.accept()
    #conn.send(str.encode('waiting for connection to be established...'))
    #pnt_lk.acquire(True)
    t = threading.Thread(target=client, args=[conn])
    # threading.thread(target=client, args=(conn))
    t.daemon =True
    t.start()

