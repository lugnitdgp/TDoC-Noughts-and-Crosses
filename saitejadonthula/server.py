
import socket
import threading

def client(c):
    try:
        print('connection established...')
        conn.send(str.encode('connection is established...'))
        while True:
            msg=c.recv(1024)
            print(msg)
            if  msg==  b'qitqowiie///':
                c.close()
                print('connection ended..')
                #pnt_lk.release()
                break
            c.send(msg)
    except :
        print('connection lost')

pnt_lk = threading.Lock()
host = ""
port = 10000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
while True:
    conn,add= s.accept()
    pnt_lk.acquire()
    t = threading.Thread(target=client, args=[conn])
    pnt_lk.release()
    t.daemon =True
    t.start()

