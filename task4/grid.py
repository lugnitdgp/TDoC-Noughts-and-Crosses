import pygame
import os

letterX = pygame.image.load(os.path.join('imgs', 'x.png')) # adding the images
letterO = pygame.image.load(os.path.join('imgs', 'o.png')) # adding the images


class Grid: #setting up the grid lines
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)), # first horizontal line
                           ((0,400), (600,400)), # second horizontal line
                           ((200,0), (200,600)), # first vertical line
                           ((400,0), (400,600))] # second vertical line

        self.grid = [[0 for x in range(3)] for y in range(3)] # creating a 3x3 matrix
        # search directions  N         NW        W       SW       S       SE      E       NE
        self.search_dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.game_over = False

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == "X":
                    surface.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x, y) == "O":
                    surface.blit(letterO, (x*200, y*200))
    def print_grid(self):  
        for row in self.grid:
            print(row)

    def get_cell_value(self, x, y): # a getter
        return self.grid[y][x]

    def set_cell_value(self, x, y, value): # a setter
        self.grid[y][x] = value

    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y) == 0:
            self.set_cell_value(x, y, player)
            self.check_grid(x, y, player)

    def is_within_bounds(self, x, y):  
        return x >= 0 and x < 3 and y >= 0 and y < 3 # if any one is false it return false
    
    def if_grid_full(self): # no one wins but game is over
        for row in self.grid:
            for value in row:
                if value == 0: 
                    return False
        return True # if all the cells are occupied we return true


    def check_grid(self, x, y, player): # the game logic
        count = 1 # local variable 
        for index, (dirx, diry) in enumerate(self.search_dirs): # return the index number
            if self.is_within_bounds(x+dirx, y+diry) and self.get_cell_value(x+dirx, y+diry) == player: # it will check in the bounds and if it doesnt get any cell it  will skip the code 
                count += 1
                new_x = x + dirx
                new_y = y + diry
                if self.is_within_bounds( new_x+dirx, new_y+diry) and self.get_cell_value( new_x+dirx, new_y+diry) == player: # updating the new directions
                    count += 1
                    if count == 3: #  the player wins
                        break
                if count < 3:
                    new_dir = 0
                    # mapping the indices to opposite direction: 0-4,, 1-5, 2-6 ,3-7, 4-0, 5-1, 6-2, 7-3
                    if index == 0:
                        new_dir = self.search_dirs[4] # N to S
                    elif index == 1:
                        new_dir = self.search_dirs[5] # NW to SE
                    elif index == 2:
                        new_dir = self.search_dirs[6] # W to E
                    elif index == 3:
                        new_dir = self.search_dirs[7] # SW to NE
                    elif index == 4:
                        new_dir = self.search_dirs[0] # S to N
                    elif index == 5:
                        new_dir = self.search_dirs[1] # SE to NW
                    elif index == 6:
                        new_dir = self.search_dirs[2] # E to W
                    elif index == 7:
                        new_dir = self.search_dirs[3] # NE to SW

                    if self.is_within_bounds(x + new_dir[0], y + new_dir[1]) \
                            and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print('Player with marker',player, 'wins!') 
            self.game_over = True  # game is over
        else:
            
            self.game_over = self.if_grid_full() 


    

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.set_cell_value(x, y, 0)

    