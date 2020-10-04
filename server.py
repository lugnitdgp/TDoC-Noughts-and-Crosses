import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port1 = 3456
port2= 10000
s.bind((host,port1))
s.listen(5)
print('waiting for client....')
con,add = s.accept()
print('connection established with a client 1 :)')
con.send(str.encode('ask 2nd client to connect....'))
t.bind((host,port2))
t.listen(5)
con2,add2= t.accept()
con.send(str.encode('connection established with client 2 :)'))
print('connection established with client 2 :)')

try:
    while True:
        cmd=con.recv(1024)
        if cmd.decode("utf-8")=='quit':
            s.close()
            strn='''your friend's connection is lost :)'''
            con2.send(str.encode(strn))
            t.close()
            sys.exit()
        con2.send(cmd)
        cmd=con2.recv(1024)
        if cmd.decode("utf-8")=='quit':
            t.close()
            strn='''your friend's connection is lost :)'''
            con.send(str.encode(strn))
            s.close()
            sys.exit()
        con.send(cmd)
except:
    print("connection lost")
