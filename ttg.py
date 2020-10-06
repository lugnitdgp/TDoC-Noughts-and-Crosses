# import numpy as np
from array import *
matrix = [[1,2,3],[4,5,6],[7,8,9]]
g = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
def ini():
    global g
    g = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
def input_to_index(n):
    if(n/3 > int(n/3)):
        i = int(n/3) 
    else:
        i = int(n/3) - 1
    if(n%3 == 0):
        j = int(n%3) + 2
    else:
        j = int(n%3) - 1
    return i,j

def printMatix(M):
    result = ''    
    for i in range(3):
        for j in range(3):
            if(M[i][j] != -1):
                result += "| " + str(M[i][j]) + " |"
            else:
                result += "|   |"
        result += '\n'  
    print(result)    
def wld(a):
    f = False
    if(g[0][0] == a):
        for x in range(3):
            if(g[0][x] == a):
                f = 1
            else:
                f = 0
                break
        if(f): return 1
    
        for x in range(3):
            if(g[x][0] == a):
                f = 1
            else:
                f = 0
                break
        if(f): return 1
        for x in range(3):
            if(g[x][x] == a):
                f = 1
            else:
                f = 0
                break
        if(f): return 1
    if(g[0][1] == a):
        if(g[0][2] == a and g[1][2] == a): return 1
        for x in range(3):
            if(g[x][1] == a):
                f = 1
            else:
                f = 0
                break
        if(f): return 1 
    if(g[0][2] == a):
        for x in range(2):
            if(g[0+x+1][2-x-1] == a):
                f = 1
            else:
                f = 0
                break                  
        if(f): return 1 
        for x in range(3):
            if(g[x ][2] == a):
                f = 1
            else:
                f = 0
                break                  
        if(f): return 1 
    if(g[1][0] == a):
        if(g[2][0] == a and g[0][0] == a): return 1
        for x in range(3):
            if(g[1][x] == a):
                f = 1
            else:
                f = 0
                break
        if(f): return 1 
    if(g[2][0] == a):
        for x in range(3):
            if(g[2][x] == a):
                f = 1
            else:
                f = 0
                break                  
        if(f): return 1                 
    return 0 
                

def game(n,a):
    # while True:
        # n = int(input())
    i,j = input_to_index(n)
    if(g[i][j] != -1):
        return True
    # print(str(n)+" i: "+str(i)+" j: "+str(j))
    g[i][j] = a
    
    printMatix(g) 
    if(wld(a)):
        print("Player " + str(a+1) + " Wins!")
        return -1
    return False

def main():
    printMatix(matrix)

    game() 

if __name__ == "__main__":
    main()