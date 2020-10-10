import pygame

class Grid:
    def __init__(self):
        self.grid_line = (
            ((160,60), (160,510)), # first vertical line
            ((310,60), (310,510)), # second vertical line
            ((10,210), (460,210)), # first horizontal line
            ((10,360), (460,360)) # second horizontal line
        )

        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.game_over = False
        self.cnt = 1
        self.res1 = [None, None]
        self.res2 = [None, None]
    
    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, val):
        if self.grid[y][x] == 0:            
            self.grid[y][x] = val
            return True

        return False

    def draw_line(self, surface):
        for line in self.grid_line:
            pygame.draw.line(surface, (255,255,255), line[0], line[1], 2)

    def draw_sign(self, surface):
        for y in range(3):
            for x in range(3):
                if self.grid[y][x] == 'X':
                    pygame.draw.line(surface, (0,235,0), (x*150 + 20, y*150 + 70), ((x+1)*150, (y+1)*150 + 50), 6)            
                    pygame.draw.line(surface, (0,235,0), ((x+1)*150, y*150 + 70), (x*150 + 20, (y+1)*150 + 50), 5)                    
                if self.grid[y][x] == 'O':
                    pygame.draw.circle(surface, (235,50,0), (x*150 + 85, y*150+135), 65, 5)
          

    def print_grid(self):
        for row in self.grid:
            print(row)

    def check(self):
        ans = None
        x = self.grid[0][0]
        self.res1 = [0,0]
        if x != 0:
            if x==self.grid[0][1] and x==self.grid[0][2]:
                ans = x
                self.res2 = [0,2]
            if x==self.grid[1][0] and x==self.grid[2][0]:
                ans = x
                self.res2 = [2,0]
            if x==self.grid[1][1] and x==self.grid[2][2]:
                ans = x
                self.res2 = [2,2]
        if ans is None:
            x = self.grid[0][1]
            self.res1 = [0,1]
            if x != 0:
                if x==self.grid[1][1] and x==self.grid[2][1]:
                    ans = x
                    self.res2 = [2,1]
        if ans is None:
            x = self.grid[0][2]
            self.res1 = [0,2]
            if x != 0:
                if x==self.grid[1][2] and x==self.grid[2][2]:
                    ans = x
                    self.res2 = [2,2]
                if x==self.grid[1][1] and x==self.grid[2][0]:
                    ans = x
                    self.res2 = [2,0]
        if ans is None:
            x = self.grid[1][0]
            self.res1 = [1,0]
            if x != 0:
                if x==self.grid[1][1] and x==self.grid[1][2]:
                    ans = x
                    self.res2 = [1,2]
        if ans is None:
            x = self.grid[2][0]
            self.res1 = [2,0]
            if x != 0:
                if x==self.grid[2][1] and x==self.grid[2][2]:
                    ans = x
                    self.res2 = [2,2]

        if ans != None:
            self.game_over = True
            self.cnt=0
        else:
            self.game_over = self.is_full()
        return ans

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]==0:
                    return False
        return True

    def clear(self):
        self.game_over = False
        self.cnt=1
        for i in range(3):
            for j in range(3):
                self.grid[i][j]=0    

    def write_text(self, text, x, y, surface, font_size):
        textSize = pygame.font.SysFont("comicsansms", font_size)
        textSurf = textSize.render(text, True, (230,230,230))
        textRect = textSurf.get_rect()
        textRect.center = (x, y)
        surface.blit(textSurf, textRect)

    def button(self, surface, msg,x,y,w,h,ic,ac):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(surface, ac,(x,y,w,h))

            if click[0] == 1:
                self.clear()     
        else:
            pygame.draw.rect(surface, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf = smallText.render(msg, True, (255,255,255))
        textRect = textSurf.get_rect()
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        surface.blit(textSurf, textRect)

    def update(self, surface,header, res):
        surface.fill((0,0,0))
        self.draw_line(surface)
        self.draw_sign(surface)
        self.write_text(header, 235, 25, surface, 25)
        if res is Not None:
            x1, y1, x2, y2 = self.res1[1], self.res1[0], self.res2[1], self.res2[0]
            pygame.draw.line(surface, (200,161,219), (x1*150 + 85, y1*150 + 135), (x2*150 + 85, y2*150 + 135), 7)
        pygame.display.update()
