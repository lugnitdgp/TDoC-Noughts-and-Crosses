import socket
s = socket.socket()
s.connect((socket.gethostbyname('localhost'), 12345))
print("Connected!")
print(str(s.recv(1024), "utf-8"))
count = 1
ans = input(">>")
s.send(str.encode(ans))
l1 = []


def play():
    while True:
        print(str(s.recv(1024), "utf-8"))
        message = input(">>")
        s.send(str.encode(message))
        try:
            i, j = message.split()
        except:
            break
        if message in l1 or int(i) >= 3 or int(j) >= 3:
            break
        l1.append(message)
        print(str(s.recv(1024), "utf-8"))
        state = str(s.recv(1024), "utf-8")
        if state != "Continue...":
            print(state)
            break
        l1.append(str(s.recv(1024), "utf-8"))
        state = str(s.recv(1024), "utf-8")
        if state != "Continue...":
            print(state)
            break
    print(str(s.recv(1024), "utf-8"))
    message2 = input(">>")
    s.send(str.encode(message2))
    if message2 == "Yes":
        l1.clear()
        play()


if ans == "Yes":
    play()
print(str(s.recv(1024), "utf-8"))
s.close()