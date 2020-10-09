import pygame
pygame.init()

cross_mark = pygame.image.load('cross.png')
round_mark = pygame.image.load('round.png')


class Grid:
    def __init__(self):
        self.grid_lines = [((0, 180), (450, 180)),      # first horizontal line
                           ((0, 360), (450, 360)),      # second horizontal line
                           ((150, 0), (150, 540)),      # first vertical line
                           ((300, 0), (300, 540))]      # second vertical line

        self.game_over = False

        self.grid = [[0 for x in range(3)] for y in range(3)]

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (0, 0, 0), line[0], line[1], 5)

        for y in range(3):
            for x in range(3):
                if self.get_cell_value(x, y) == 'X':
                    surface.blit(cross_mark, (x*150, y*180))
                elif self.get_cell_value(x, y) == 'O':
                    surface.blit(round_mark, (x*150, y*180))

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y) == 0:
            self.set_cell_value(x, y, player)
            self.check_grid(player)

    def check_grid(self, player):
        for y in range(3):
            if self.grid[y][0] == self.grid[y][1] == self.grid[y][2] == player:
                self.game_over = True
                return
        for x in range(3):
            if self.grid[0][x] == self.grid[1][x] == self.grid[2][x] == player:
                self.game_over = True
                return
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == player:
            self.game_over = True
            return
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == player:
            self.game_over = True
            return
        else:
            self.game_over = self.is_grid_full()

    def is_grid_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def clear_grid(self):
        for y in range(3):
            for x in range(3):
                self.set_cell_value(x, y, 0)
