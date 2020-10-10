import socket
import pygame
import time,sys,os
import time
from pygame.locals import *
#from n import Network
pygame.init()
size = width, height = 600,600
fps=30
CLOCK =pygame.time.Clock() 
#Color codes
black = 0, 0, 0
white=255,255,255
red = (255,0,0)
cyan=(0, 255, 255)
#***********************************************************************************
#IMAGES
game_cover = pygame.image.load("covergame.png") 
x_img = pygame.image.load("x.png") 
o_img = pygame.image.load("o.png") 
   
# resizing images 
game_cover = pygame.transform.scale(game_cover, (width, height)) 
x_img = pygame.transform.scale(x_img, (200,200)) 
o_img = pygame.transform.scale(o_img, (200,200)) 
#************************************************************************************

class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)), # first horizontal line
            ((0, 400), (600,400)), # second horizontal line
            ((200, 0), (200,600)), # first vertical line
            ((400, 0), (400,600))] #second vertical line
        self.grid=[[0 for x in range(3)] for y in range(3)]
        self.game_ended=False
        # search directions  N         NW        W       SW       S       SE      E       NE
        self.search_directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

#***********************************************************************************  
    def draw(self,surface):
        
        for line in self.grid_lines:
            pygame.draw.line(surface,white,line[0],line[1],3)
            #pygame.display.flip()
        for y in range(len(self.grid)):
                for x in range(len(self.grid[y])):
                    if self.get_cell_value(x,y)=='X':
                        surface.blit(x_img,(x*200,y*200))
                        
                    elif self.get_cell_value(x,y)=='O':
                        surface.blit(o_img,(x*200,y*200))
                       

            
    def get_cell_value(self,x,y):
        return self.grid[y][x]
    
    def set_cell_value(self,x,y,value):
        self.grid[y][x]=value
    
    def print_grid(self):
        for row in self.grid:
            print(row)

    def get_mouse(self,x,y,player):
        #checks if the chosen position is empty then only one can mark that POSITION
        if self.get_cell_value(x,y)== 0: 
            self.set_cell_value(x,y,player)
            self.check_win(x,y,player)
#***********************************************************************************
#checks if the clicked position is inside the game window
    def check_boundary(self,x,y):
        if x>=0 and x<3 and y>=0 and y<3:
            return True
        
#***********************************************************************************           
                
    def check_win(self,x,y,player):
        count = 1
        for index, (dirx, diry) in enumerate(self.search_directions):
            if self.check_boundary(x+dirx, y+diry) and self.get_cell_value(x+dirx, y+diry) == player:
                count += 1
                xx = x + dirx
                yy = y + diry
                if self.check_boundary(xx+dirx, yy+diry) and self.get_cell_value(xx+dirx, yy+diry) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0
                    # mapping the indices to opposite direction: 0-4 1-5 2-6 3-7 4-0 5-1 6-2 7-3
                    if index == 0:
                        new_dir = self.search_directions[4] # N to S
                    elif index == 1:
                        new_dir = self.search_directions[5] # NW to SE
                    elif index == 2:
                        new_dir = self.search_directions[6] # W to E
                    elif index == 3:
                        new_dir = self.search_directions[7] # SW to NE
                    elif index == 4:
                        new_dir = self.search_directions[0] # S to N
                    elif index == 5:
                        new_dir = self.search_directions[1] # SE to NW
                    elif index == 6:
                        new_dir = self.search_directions[2] # E to W
                    elif index == 7:
                        new_dir = self.search_directions[3] # NE to SW

                    if self.check_boundary(x + new_dir[0], y + new_dir[1]) \
                            and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print(player, 'wins!')
            self.game_ended = True #stops player to do further moves 
        else:
            self.game_ended = self.board_full() # draw condition 
#************************************************************************************
            
    def board_full(self):
        for row in self.grid:
            for val in row:
                if val==0:    #if the cell is empty then board is not full
                    return False
            return True #after checking all the cells if all are full then returns true

#***********************************************************************************        
    def reset_grid(self):
   # it resets the value of every cell to zero 
        for y in range(len(self.grid)):
                       for x in range(len(self.grid[y])):
                                      self.set_cell_value(x,y,0)
#***********************************************************************************                                      
    
       
    


          
                
               
        
            

             
            
        
        
            










