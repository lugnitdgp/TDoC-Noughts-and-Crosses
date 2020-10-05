l1 = [[' ' for i in range(3)] for i in range(3)]

def game():
    print("""
           |           |         
     {0}     |     {1}     |     {2}  
______(0,0)|______(0,1)|______(0,2)
           |           |
     {3}     |     {4}     |     {5}   
______(1,0)|______(1,1)|______(1,2)
           |           |
     {6}     |     {7}     |     {8}
      (2,0)|      (2,1)|      (2,2)""".format(l1[0][0], l1[0][1], l1[0][2], l1[1][0], l1[1][1], l1[1][2], l1[2][0], l1[2][1], l1[2][2]))

def check(player):
    flag = False
    for i in range(3):
        if l1[i][0] == l1[i][1] and l1[i][1] == l1[i][2] and l1[i][2] == l1[i][0] and (l1[i][0] == 'x' or l1[i][0] == 'o'):
            flag = True
            print(player, "wins!")
            break
        if l1[0][i] == l1[1][i] and l1[1][i] == l1[2][i] and l1[2][i] == l1[0][i] and (l1[0][i] == 'x' or l1[0][i] == 'o'):
            flag = True
            print(player, "wins!")
            break
    if l1[0][0] == l1[1][1] and l1[1][1] == l1[2][2] and l1[2][2] == l1[0][0] and (l1[0][0] == 'x' or l1[0][0] == 'o'):
        flag = True
        print(player, "wins!")
    if l1[0][2] == l1[1][1] and l1[1][1] == l1[2][0] and l1[2][0] == l1[0][2] and (l1[1][1] == 'x' or l1[1][1] == 'o'):
        flag = True
        print(player, "wins!")
    if ' ' not in [l1[0][0], l1[0][1], l1[0][2], l1[1][0], l1[1][1], l1[1][2], l1[2][0], l1[2][1], l1[2][2]] and flag != True:
        flag = True
        print("Draw!")
    return flag

player = 'a'
shit = False
while(shit == False):
    game()
    i, j = input("{}:>>".format(player)).split()
    if player == 'a':
        l1[int(i)][int(j)] = 'x'
    else:
        l1[int(i)][int(j)] = 'o'
    shit = check(player)
    if player == 'a':
        player = 'b'
    else:
        player = 'a'
game()