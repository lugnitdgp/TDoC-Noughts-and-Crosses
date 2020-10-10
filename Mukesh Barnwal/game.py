class game:
    def __init__(self):
        self.board = [None,None, None, None,None, None,None,None, None]

    def check(self):
        x = self.board[0]
        if x is not None:
            if x==self.board[1] and x==self.board[2]:
                return x
            if x==self.board[4] and x==self.board[8]:
                return x
            if x==self.board[3] and x==self.board[6]:
                return x
        x = self.board[1]
        if x is not None:
            if x==self.board[4] and x==self.board[7]:
                return x
        
        x = self.board[2]
        if x is not None:
            if x==self.board[5] and x==self.board[8]:
                return x
            if x==self.board[4] and x==self.board[6]:
                return x
        
        x = self.board[3]
        if x is not None:
            if x==self.board[4] and x==self.board[5]:
                return x

        x = self.board[6]
        if x is not None:
            if x==self.board[7] and x==self.board[8]:
                return x

        return None

    def put(self, x, ch):
        self.board[x-1] = ch

    def print_board(self):
        for x in range(9):
            if self.board[x] is not None:
                print('| ' + self.board[x] + ' |', end='')
            else:
                print('|   |', end='')
            if (x+1)%3==0:
                print('')