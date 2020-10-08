import socket
import threading
import sys

def threaded(s):
    while True:
        data = input('>')
        if data==' ':
            print('bye..')
            s.send(str.encode('qitqowiie///'))
            s.close()
            sys.exit()

        s.send(str.encode(data))

        print(s.recv(1024).decode('utf-8'))


pnt_lk = threading.Lock()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),10000))
#print(s.recv(1024).decode())
print(s.recv(1024).decode())
pnt_lk.acquire()
t = threading.Thread(target=threaded,args=(s,))
pnt_lk.release()
t.start()






