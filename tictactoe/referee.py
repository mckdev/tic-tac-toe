import re
import sys


class Referee:
    """Watches the grid and validates user inputs.

    Every human input and AI decision should be validated and processed by the
    Referee before it can be applied on the grid.

    The referee also checks the grid at the end of each turn and exits the game
    when win condition was met or when the grid is fully occupied.
    
    Args:
        game (Game): Game instance which initialized the Referee.
    
    Attributes:
        grid (Grid): Grid instance to be watched by the Referee.
    
    """
    def __init__(self, game):
        print('Initializing Referee ...')
        self.game = game
        self.grid = game.grid

    def validate_input(self, data, player):
        """Validates user input and returns True if it's valid.
        
        Args:
            data (str): String input from the player or AI to be validated.
            player (Player): Player instance which sent the input.
        """
        cleaned_data = data.replace(' ', '').strip()
        # Check if stripped input matches regex pattern.
        if re.search(r'^\d\,\d$', cleaned_data):
            pass    # Pattern matched, continue validation.
        else:
            print('Referee says:',
                  '"Nope! You must provide input in "<row>,<col>" format."' )
            print('Try again:', end=' ')
            return

        # Check if values are in range of grid.
        xy = cleaned_data.split(',')
        for val in xy:
            if not 0 <= int(val) <= self.grid.size - 1:
                print('Referee says:',
                      '"Nope! You must provide values which fit on the grid."' )
                print('Try again:', end=' ')
                return
        
        # Check if grid position is occupied.
        x = int(xy[0])
        y = int(xy[1])
        if not self.grid.is_occupied(x, y):
            print('Referee says: "OK! Player {} takes position ({},{})."'\
                  .format(player.char, x, y))
            return True  # Confirm move.
        else:
            print('Referee says: "Nope! This position is already taken."' )
            print('Try again:', end=' ')
        
    def process_input(self, data):
        """Process string input from player or AI and return pair of ints which
        repersent x, y position to be taken the grid.

        This method expects that input string was already validated by
        `validate_input` method and that the data is correct.
        
        Args:
            data (Data): String input from the player or AI to be processed.
        """
        cleaned_data = data.replace(' ', '').strip()
        xy = cleaned_data.split(',')
        x = int(xy[0])
        y = int(xy[1])        
        return x, y
    
    def check_for_winner(self):
        """Check the grid field by field and exit the game with SystemExit
        if three adjacent characters of the same player were found in 
        horizontal, vertical or diagonal line.
        
        The check is skipped for occupied positions and corners of the grid.

        Bottom and top row positions are checked against adjacent horizontal
        characters while left and right most rows are only checked vertically.

        Remaining positions are checked against all adjacent positions.
        """
        grid = self.grid
        for x in range(grid.size):
            for y in range(grid.size):
                if len(grid[x][y]) > 0: # Only check if position is taken
                    # Skip check if in the corner of the grid
                    if x == 0 and y == 0:   
                        # Top left
                        continue
                    if x == 0 and y == grid.size - 1:
                        # Top right
                        continue
                    if x == grid.size - 1 and y == 0:
                        # Bottom left
                        continue
                    if x == grid.size - 1 and y == grid.size - 1:
                        # Bottom right
                        continue
                    
                    # Check only horizontally when on the top and bottoms rows.
                    if x == 0 or x == grid.size - 1:
                        # print('Checking horizontally on', x, y)
                        if self.horizontal_check(x, y):
                            self.grid.show()
                            print('{} IS THE WINNER!'.format(grid[x][y]))
                            print('\nGame finished in {} turns.'\
                                  .format(self.game.completed_turns))
                            sys.exit()
                    # Check only vertically when on the left or right most cols.
                    elif y == 0 or y == grid.size - 1:
                        if self.vertical_check(x, y):
                            self.grid.show()
                            print('{} IS THE WINNER!'.format(grid[x][y]))
                            print('\nGame finished in {} turns.'\
                                  .format(self.game.completed_turns))
                            sys.exit()
                    # Check in all directions when elsewhere.
                    else:
                        if self.horizontal_check(x, y) or\
                           self.vertical_check(x, y) or\
                           self.diagonal_check(x, y):
                            self.grid.show()
                            print('{} IS THE WINNER!'.format(grid[x][y]))
                            print('\nGame finished in {} turns.'\
                                  .format(self.game.completed_turns))
                            sys.exit()
                
    def horizontal_check(self, x, y):
        """Returns True if three adjacent horizontal positions are the same.
        
        Takes row and col index and checks two adjacent horizontal positions.

        Args:
            x (int): Represents row number on the grid.
            y (int): Represents col number on the grid.
        """
        grid = self.grid
        if grid[x][y] == grid[x][y-1] == grid[x][y+1]:
            return True

    def vertical_check(self, x, y):
        """Returns True if three adjacent vertical positions are the same.
        
        Takes row and col index and checks two adjacent vertical positions.

        Args:
            x (int): Represents row number on the grid.
            y (int): Represents col number on the grid.
        """
        grid = self.grid
        if grid[x][y] == grid[x-1][y] == grid[x+1][y]:
            return True      

    def diagonal_check(self, x, y):
        """Returns True if three adjacent diagonal positions are the same.
        
        Takes row and col index and checks two adjacent diagonal positions
        in two possible combinations.

        Args:
            x (int): Represents row number on the grid.
            y (int): Represents col number on the grid.
        """
        grid = self.grid
        if grid[x][y] == grid[x-1][y-1] == grid[x+1][y+1] or \
           grid[x][y] == grid[x-1][y+1] == grid[x+1][y-1]:
            return True

    def check_for_full_grid(self):
        """Exits the game if the grid is fully occupied."""
        grid = self.grid
        if grid.is_full():
            self.grid.show()
            print('YOU ARE ALL LOSERS!')
            print('\nGrid full. Game finished in {} turns.'\
                  .format(self.game.completed_turns))
            sys.exit()
