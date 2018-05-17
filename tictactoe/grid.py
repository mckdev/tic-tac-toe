from collections import UserList


class Grid(UserList):
    def __init__(self, size):
        print('Initializing {0}x{0} grid ...'.format(size))
        self.size = int(size)
        self.create()
    
    def create(self):
        grid = []
        for x in range(self.size):
            grid.append([])
            for y in range(self.size):
                grid[x].append('')
        self.data = grid

    def show(self):
        grid = self.data
        print('\n\t', end='')
        for x in range(self.size):
            print('    {}\t'.format(x), end='')
        print('\r')
        print('\t', '--------' * self.size)
        for x in range(self.size):
            print('   ',x, end='\t')
            for y in range(self.size):
                print('|  ', grid[x][y], end='\t')
            print('|\r')
            print('\t', '--------' * self.size)
            
        print('\r')

    def update(self, row, col, char):
        self.data[row][col] = char

    def is_full(self):
        occupied = [field for field in self.flat() if len(field) == 1]
        return len(occupied) >= len(self.flat())

    def is_occupied(self, x, y):
        if self.data[x][y]:
            return True

    def flat(self):
        return [ item for sublist in self.data for item in sublist ]
