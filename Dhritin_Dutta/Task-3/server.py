import socket
s = socket.socket()
s.bind(('', 12345))
s.listen()
c, addr = s.accept()
print("Connected to", addr)
message = """# ====================#
# NOUGHTS AND CROSSES #
# ====================#

Enter the space separated coordinates of where you want to mark on the grid. Send anything else(or wrong coordinates to quit) to quit. Should we start?(Yes/<Anything else>)"""
print(message)
c.send(str.encode(message))
l1 = [[' ' for i in range(3)] for i in range(3)]
l2 = []

def game():
    message = """
           |           |         
     {0}     |     {1}     |     {2}  
______(0,0)|______(0,1)|______(0,2)
           |           |
     {3}     |     {4}     |     {5}   
______(1,0)|______(1,1)|______(1,2)
           |           |
     {6}     |     {7}     |     {8}
      (2,0)|      (2,1)|      (2,2)""".format(l1[0][0], l1[0][1], l1[0][2], l1[1][0], l1[1][1], l1[1][2], l1[2][0], l1[2][1], l1[2][2])
    print(message)
    c.send(str.encode(message))
        

def check(player):
    flag = False
    for i in range(3):
        if l1[i][0] == l1[i][1] and l1[i][1] == l1[i][2] and l1[i][2] == l1[i][0] and (l1[i][0] == 'x' or l1[i][0] == 'o'):
            flag = True
            print(player, "wins!")
            c.send(str.encode(player + " wins!"))
            break
        if l1[0][i] == l1[1][i] and l1[1][i] == l1[2][i] and l1[2][i] == l1[0][i] and (l1[0][i] == 'x' or l1[0][i] == 'o'):
            flag = True
            print(player, "wins!")
            c.send(str.encode(player + " wins!"))
            break
    if l1[0][0] == l1[1][1] and l1[1][1] == l1[2][2] and l1[2][2] == l1[0][0] and (l1[0][0] == 'x' or l1[0][0] == 'o'):
        flag = True
        print(player, "wins!")
        c.send(str.encode(player + " wins!"))
    if l1[0][2] == l1[1][1] and l1[1][1] == l1[2][0] and l1[2][0] == l1[0][2] and (l1[1][1] == 'x' or l1[1][1] == 'o'):
        flag = True
        print(player, "wins!")
        c.send(str.encode(player + " wins!"))
    if ' ' not in [l1[0][0], l1[0][1], l1[0][2], l1[1][0], l1[1][1], l1[1][2], l1[2][0], l1[2][1], l1[2][2]] and flag != True:
        flag = True
        print("Draw!")
        c.send(str.encode("Draw!"))
    if flag == False:
        c.send(str.encode("Continue..."))
    return flag
    

def play():
    t_f = False
    while t_f == False:
        game()
        reply = str(c.recv(1024), "utf-8")
        if reply in l2:
            break
        l2.append(reply)
        try:
            i, j = reply.split()
            l1[int(i)][int(j)] = 'x'
        except:
            break
        game()
        t_f = check('Client')
        if t_f == True:
            break
        i, j = input(">>").split()
        l2.append(i + ' ' + j)
        c.send(str.encode(i + ' ' + j))
        l1[int(i)][int(j)] = 'o'
        t_f = check('Server')
    c.send(str.encode("Play again? (Yes/<anything else>)"))
    if str(c.recv(1024), "utf-8") == "Yes":
        l2.clear()
        for i in range(3):
            for j in range(3):
                l1[i][j] = ' '
        play()
    

ans = str(c.recv(1024), "utf-8")
if ans == "Yes":
    play()
c.send(str.encode("Closing connection..."))
s.close()