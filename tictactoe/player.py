from random import choice, shuffle


class Player:
    def __init__(self, player):
        print('Initializing Player', player['char'], end=' ')
        self.char = player['char']
        try:
            self.ai = player['ai']
        except KeyError:
            # Set AI to false if it was not present in the config.
            self.ai = False
        if self.ai:
            print('(AI) ...')
        else:
            print(' ...')

    def move(self):
        """Ask human player for input and return it."""
        return input()

    def ai_move(self, grid):
        """Decide move of the AI on a given grid and return decision as string
        in x,y format as expected by the Referee."""
        decision = self.ai_decide(grid)  # Try intelligent decision...
        if decision == None:
            # Pick a random free position if no decision was made.
            free_positions = []
            for x in range(grid.size):
                for y in range(grid.size):
                    if not grid.is_occupied(x, y):
                        free_positions.append('{},{}'.format(x, y))
            return choice(free_positions)
        return decision 

    def ai_decide(self, grid):
        """Crawls the grid checking all non-occupied fields and takes first
        opportunity to win or block an opponent from winning.
        
        Returns decision as string in x,y format or None if there was no
        opportunity to win or block an opponent.

        Before starting the crawl, it shuffles the rows and cols of the grid
        to randomize the order in which they are checked.

        Args:
            grid (Grid): The grid instance on which the move has to take place.
        """
        rows = [x for x in range(grid.size)]
        cols = [x for x in range(grid.size)]
        shuffle(rows)
        shuffle(cols)
        for x in range(grid.size):
            for y in range(grid.size):
                # Only check if position is not occupied
                if not grid.is_occupied(x, y):
                    # print('Checking', x, y)

                    if x == 0 and y == 0:
                        # Top left corner
                        if self.ai_check_right(x, y, grid) or \
                           self.ai_check_bottom_right(x, y, grid) or \
                           self.ai_check_below:
                            return '{},{}'.format(x, y)
                        continue

                    elif x == 0 and y == grid.size - 1:
                        # Top right corner
                        if self.ai_check_left(x, y, grid) or \
                           self.ai_check_bottom_left(x, y, grid) or \
                           self.ai_check_below(x, y, grid):
                            return '{},{}'.format(x, y)
                        continue

                    elif x == grid.size - 1 and y == 0:
                        # Bottom left corner
                        if self.ai_check_above(x, y, grid) or \
                           self.ai_check_top_right(x, y, grid) or \
                           self.ai_check_right(x, y, grid):
                            return '{},{}'.format(x, y)
                        continue

                    elif x == grid.size - 1 and y == grid.size - 1:                            
                        # Bottom right corner
                        if self.ai_check_above(x, y, grid) or \
                          self.ai_check_top_left(x, y, grid) or \
                          self.ai_check_left(x, y, grid):
                            return '{},{}'.format(x, y)
                        continue

                    elif x == 0:  
                        # Top row except corners
                        if self.ai_check_horizontal(x, y, grid) or \
                           self.ai_check_below(x, y, grid):
                            return '{},{}'.format(x, y)
                        if y > 1:  
                            # If at least two positions from the left wall
                            if self.ai_check_left(x, y, grid) or \
                               self.ai_check_bottom_left(x, y, grid):
                                return '{},{}'.format(x, y)
                        if y < grid.size - 2:  
                            # If at least two positions from the right wall
                            if self.ai_check_right(x, y, grid) or \
                               self.ai_check_bottom_right(x, y, grid):
                                return '{},{}'.format(x, y)

                    elif x == grid.size - 1:  
                        # Bottom row except corners
                        if self.ai_check_horizontal(x, y, grid) or \
                           self.ai_check_above(x, y, grid):
                            return '{},{}'.format(x, y)
                        if y > 1:  
                            # If at least two positions from the left wall
                            if self.ai_check_left(x, y, grid) or \
                               self.ai_check_top_left(x, y, grid):
                                return '{},{}'.format(x, y)
                        if y < grid.size - 2:  
                            # If at least two positions from the right wall
                            if self.ai_check_right(x, y, grid) or \
                               self.ai_check_top_right(x, y, grid):
                                return '{},{}'.format(x, y)
                            
                    elif y == 0:
                        # Left wall except corners
                        if self.ai_check_vertical(x, y, grid) or \
                           self.ai_check_right(x, y, grid):
                            return '{},{}'.format(x, y)
                        if x > 1:
                            # If at least two positions from the top
                            if self.ai_check_above(x, y, grid) or \
                               self.ai_check_top_right(x, y, grid):
                                return '{},{}'.format(x, y)
                        if x < grid.size - 2:
                            # If at least two positions from the bottom
                            if self.ai_check_below(x, y, grid) or \
                               self.ai_check_bottom_right(x, y, grid):
                                return '{},{}'.format(x, y)
                        
                    elif y == grid.size - 1:
                        # Right wall except corners
                        if self.ai_check_vertical(x, y, grid) or \
                           self.ai_check_left(x, y, grid):
                            return '{},{}'.format(x, y)
                        if x > 1:
                            # If at least two positions from the top
                            if self.ai_check_above(x, y, grid) or \
                               self.ai_check_top_left(x, y, grid):
                                return '{},{}'.format(x, y)
                        if x < grid.size - 2:
                            # If at least two positions from the bottom
                            if self.ai_check_below(x, y, grid) or \
                               self.ai_check_bottom_left(x, y, grid):
                                return '{},{}'.format(x, y)                        

                    else:
                        # Any other position except corners and walls - do all the checks
                        if self.ai_check_horizontal(x, y, grid) or \
                           self.ai_check_vertical(x, y, grid) or \
                           self.ai_check_diagonal(x, y, grid):
                            return '{},{}'.format(x, y)
                        if x > 1:
                            # If at least two positions from the top
                            if self.ai_check_above(x, y, grid):
                                return '{},{}'.format(x, y)
                        if x < grid.size - 2:
                            # If at least two positions from the bottom
                            if self.ai_check_below(x, y, grid):
                                return '{},{}'.format(x, y)
                        if y > 1:
                            # If at least two positions from the left wall
                            if self.ai_check_left(x, y, grid):
                                return '{},{}'.format(x, y)
                        if y < grid.size - 2:
                            # If at least two positions from the right wall
                            if self.ai_check_right(x, y, grid):
                                return '{},{}'.format(x, y)                              
                        if x > 1 and y > 1:
                            # If at least two positions from the top and left
                            if self.ai_check_top_left(x, y, grid):
                                return '{},{}'.format(x, y)                                   
                        if x > 1 and y < grid.size - 2:
                            # If at least two positions from the top and right
                            if self.ai_check_top_right(x, y, grid):
                                return '{},{}'.format(x, y)
                        if x < grid.size - 2 and y > 1:
                            # If at least two positions from the bottom and left
                            if self.ai_check_bottom_left(x, y, grid):
                                return '{},{}'.format(x, y)                                   
                        if x < grid.size - 2 and y < grid.size - 2:
                            # If at least two positions from the bottom and right
                            if self.ai_check_bottom_right(x, y, grid):
                                return '{},{}'.format(x, y)                                                           

    def ai_check_horizontal(self, x, y, grid):
        """Returns if adjacent horizontal positions are taken by the same char."""
        if grid[x][y-1] and grid[x][y+1]:
            return grid[x][y-1] == grid[x][y+1]

    def ai_check_vertical(self, x, y, grid):
        """Returns if adjacent vertical positions are taken by the same char."""
        if grid[x+1][y] and grid[x-1][y]:
            return grid[x+1][y] == grid[x-1][y]
    
    def ai_check_diagonal(self, x, y, grid):
        """Returns if adjacent diagonal positions are taken by the same char."""
        if (grid[x-1][y-1] and grid[x+1][y-2]) or (grid[x+1][y-1] and grid[x-1][y+1]):
            return grid[x-1][y-1] == grid[x+1][y-2] or grid[x+1][y-1] == grid[x-1][y+1]

    def ai_check_above(self, x, y, grid):
        """Returns if both positions above are taken by the same char."""
        if grid[x-1][y] and grid[x-2][y]:
            return grid[x-1][y] == grid[x-2][y]
    
    def ai_check_top_right(self, x, y, grid):
        """Returns if both positions to the top-right are taken by the same char."""
        if grid[x-1][y+1] and grid[x-2][y+2]:
            return grid[x-1][y+1] == grid[x-2][y+2]

    def ai_check_right(self, x, y, grid):
        """Returns if both positions to the right are taken by the same char."""
        if grid[x][y+1] and grid[x][y+2]:
            return grid[x][y+1] == grid[x][y+2]

    def ai_check_bottom_right(self, x, y, grid):
        """Returns if both positions to the bottom-right are taken by the same char."""
        if grid[x+1][y+1] and grid[x+2][y+2]:
            return grid[x+1][y+1] == grid[x+2][y+2]

    def ai_check_below(self, x, y, grid):
        """Returns if both positions below are taken by the same char."""
        if grid[x+1][y] and grid[x+2][y]:
            return grid[x+1][y] == grid[x+2][y]

    def ai_check_bottom_left(self, x, y, grid):
        """Returns if both positions to the bottom-left are taken by the same char."""
        if grid[x+1][y-1] and grid[x+2][y-2]:
            return grid[x+1][y-1] == grid[x+2][y-2]        

    def ai_check_left(self, x, y, grid):
        """Returns if both positions to the left are taken by the same char."""
        if grid[x][y-1] and grid[x][y-2]:
            return grid[x][y-1] == grid[x][y-2]

    def ai_check_top_left(self, x, y, grid):
        """Returns if both positions to the top-left are taken by the same char."""
        if grid[x-1][y-1] and grid[x-2][y-2]:
            return grid[x-1][y-1] == grid[x-2][y-2]
