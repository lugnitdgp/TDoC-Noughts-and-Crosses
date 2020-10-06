from tabulate import tabulate
import socket
import threading

global l
global b
b=[0,8,1,7,2,6,3,5]
def pri():
  print(tabulate([[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]]],tablefmt="fancy_grid"))

def chk():

  if l[4] != ' ':
       for i in range(0,8,2):
            if l[ b[i]]==l[4]:
                 if l[b[i+1]]==l[4]:
                      l[ b[i] ]="*"
                      l[b[i+1]]="*"
                      l[4]="*"
                      return  1
  if l[0] != ' ':

       if l[0]==l[1] and l[0]==l[2]:
            l[0]="*"
            l[1]="*"
            l[2]="*"
            return 1
       elif l[0]==l[3] and l[0]==l[6]:

            l[0] = "*"
            l[3] = "*"
            l[6] = "*"
            return 1
  if l[8] != ' ':
       if l[8]==l[5] and l[8]==l[2]:
            l[8]="*"
            l[5]="*"
            l[2]="*"
            return 1
       elif l[8]==l[7] and l[8]==l[6]:
            l[8] = "*"
            l[7] = "*"
            l[6] = "*"
            return 1
  else:
    return 0

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ""
port = 10000
s.bind((host,port))
s.listen(1)
conn,addr = s.accept()
print("connection has been established..")
print("print the number in the box to select the box .")
l =[i+1 for i in range(9)]
pri()
l = [' ']*9
global k
k=[]
print("let's start the fun !")
g=0
for i in range(4):
  inp = input('enter the number to select a box : ')
  while inp in k:
      print('choose a valid number..')
      inp = input(': ')

  k.append(inp)
  conn.send(str.encode(inp))
  inp=int(inp)-1
  l[inp]="O"
  #pri()
  if chk():
    print('you won the game 🥳🥳🥳! ')
    pri()
    s.close()
    g=1
    break
  pri()
  print('other players move :')
  inp=conn.recv(1024).decode('utf-8')
  k.append(inp)
  inp=int(inp)-1
  l[inp]="X"
  if chk():
   print('you lost the game ☹️☹️!')
   pri()
   s.close()
   g=1
   break
  pri()
if g != 1:
    inp = input('enter the number to select a box : ')
    while inp in k:
        print('choose a valid number..')
        inp = input(': ')

    k.append(inp)
    conn.send(str.encode(inp))
    inp = int(inp) - 1
    l[inp] = "O"
    # pri()
    if chk():
        print('you won the game 🥳🥳🥳! ')
        pri()
        s.close()
        b = 1

    pri()

if g!=1:
    print("DRAW !!")
    s.close()
i=input('enter to close..')