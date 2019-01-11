
class GameGrid(object):
    
    def __init__(self):
        self.grid = [[0]*10 for i in range(10)]
        
        for x in range(0,10):
            for y in range(0,10):
                self.grid[x][y] = str(x) + str(chr(y+65))
        
    def print_grid(self):
        print()
        print("---------------------------------------------------")
        for row in self.grid:
            print("| ", end='')
            for col in row:
                print( str(col)+" | ", end='')
            print()
            print("---------------------------------------------------")
        print()
        
letter = chr(65)
gg = GameGrid()
gg.print_grid()
