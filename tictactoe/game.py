from random import shuffle

from .grid import Grid
from .player import Player
from .referee import Referee


class Game:
    def __init__(self, config):
        print('Starting new game ...')
        self.config = config
        self.completed_turns = 0
        self.init_grid()
        self.init_players()
        self.init_referee()

    def init_grid(self):
        self.grid = Grid(self.config['grid']['size'])

    def init_players(self):
        player_dict = self.config['players']
        self.players = [ Player(player_dict[player]) for player in player_dict ]

    def init_referee(self):
        self.referee = Referee(self)

    def run(self):
        players = self.players
        grid = self.grid
        referee = self.referee
        
        shuffle(players)  # Randomize who starts
        round_ = 1

        # Main game loop
        while True:
            turn = 1 # Turn count should reset after every round
            for player in players:
                print('\nRound {}, Turn {}:'.format(round_,turn))
                grid.show()
                print('Player', player.char, end=': ')

                # Make move depending on player type
                if player.ai:
                    player_input = player.ai_move(grid)  # AI needs to know the grid
                    print(player_input)
                else:
                    player_input = player.move()

                while not referee.validate_input(player_input, player):
                    # Keep asking for input until Referee accepts it
                    if player.ai:
                        player_input = player.ai_move(grid)
                        print(player_input)
                    else:
                        player_input = player.move()

                # Transform validated input into x and y
                x, y = referee.process_input(player_input)

                grid.update(x, y, player.char)
                self.completed_turns += 1
                turn += 1
                referee.check_for_winner()
                referee.check_for_full_grid()
            # All players made their turn
            round_ +=1
