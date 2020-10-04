import socket
import os
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='localhost'
port=9999

command=input()
if command=='send':
    try:
        print("binding the port "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket finding error "+str(msg)+"\n"+ "Retrying....")
        
    conn,address=s.accept()
    print("Connection is established "+" IP  "+address[0]+" port  "+str(address[1]))
    conn.send(bytes('Welcome','utf-8'))
    while True:
        print('input stuff please')
        send_msg=input()
        conn.send(bytes(send_msg,'utf-8'))
        
        print('listening')
        msg=conn.recv(1024).decode()
        if msg=='quit':
            break
        print(msg)

        
elif command=='receive' :
    
    print("connect")
    s.connect((host,port))
    data = s.recv(8).decode() # this seems to be needed to first connect
    print("connected")

    while True:
        print('listening')
        s.setblocking(True)
        data = s.recv(1024).decode()
        print(data)
        
        print('input stuff please')
        data=input()
        if data=='quit' :
            s.close()
            break
        s.send(bytes(data,'utf-8'))

        
