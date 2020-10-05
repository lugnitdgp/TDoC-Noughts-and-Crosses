# IT'S YOUR FRIEND WORK IF THE CLIENT1 IS LISTENING


import socket


s = socket.socket()
host = "192.168.1.9" 


'''
THIS IS THE IP ADDRESS OF THE HOST. IN OUR CASE WE HAVE USED THE IP ADDRESS EXPLICITLY.

ONCE THE VM IS READY AND HOST IS PLACED THERE, THE IP ADRESS OF THE SERVER WILL GO IN HERE AS IT WILL BE STATIC

'''


port = 9999  # Port to listen on (non-privileged ports are > 1023)

s.connect((host, port))  # binding the socket in client file
print('Connected to server-> IP: ', host)


while True:
    #SENDING THE DATA TO SERVER
    data = input('say=> ')

    #if empty string is entered
    if data == '':
        print("exiting>>>")
        s.send(str.encode(data))

        s.close()
        break

    s.send(str.encode(data))  # sending to server

    message_received = str(s.recv(1024), 'utf-8')

    print("messaged received from server:\n", message_received, '\n')
