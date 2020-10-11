import socket
import threading


def send():
    global cli_sock , connection
    while True:
        msg = input()
        if(msg=='quit'):
            cli_sock.send(msg.encode("utf-8"))
            connection = False
            exit()
        print("YOU >>> " + msg)
        data = []
        for i in range(len(msg)):
            if(ord(msg[i])>=65 and ord(msg[i])<=90):
                num = ord(msg[i])
                num += 10
                if(num<=100 and num>90):
                    num = 64 + num - 90
                data.append(chr(num))
            elif(ord(msg[i])>=97 and ord(msg[i])<=122):
                num = ord(msg[i])
                num += 10
                if(num<=132 and num>122):
                    num = 96 + num - 122
                data.append(chr(num))
            else:
                data.append(msg[i])
        msg = "".join(data)
        cli_sock.send(msg.encode("utf-8"))


def receive():
    global connection , cli_sock
    while True:
        if(connection == False):
            cli_sock.close()
            exit()
        if(connection == True):
            sen_name = cli_sock.recv(1024).decode()
            msg = cli_sock.recv(1024).decode()
            data = []
            for i in range(len(msg)):
                if(ord(msg[i])>=65 and ord(msg[i])<=90):
                    num = ord(msg[i])
                    num -= 10
                    if(num<65):
                        num = 91 - (65 - num)
                    data.append(chr(num))
                elif(ord(msg[i])>=97 and ord(msg[i])<=122):
                    num = ord(msg[i])
                    num -= 10
                    if(num<97):
                        num = 123 - (97 - num)
                    data.append(chr(num))
                else:
                    data.append(msg[i])
            msg = "".join(data)
            print(str(sen_name) + ' >>> ' + str(msg))


if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')
    print("Type 'quit' to quit anytime you want : ")
    uname = input('Enter your name to enter the chat > ')
    cli_sock.send(uname.encode("utf-8"))
    connection = True

    thread_send = threading.Thread(target=send)
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
