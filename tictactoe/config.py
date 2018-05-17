import json
import os.path
import sys
from collections import UserDict
from json import JSONDecodeError


class GameConfig(UserDict):
    """Initiates, validates and holds config variables in a dict."""
    def __init__(self, filename):
        print('Loading config from file ...')
        self.data = self.from_json(filename)

    def from_json(self, filename):
        try:
            project_path = os.path.abspath(os.path.dirname(__file__))
            config_path = os.path.join(project_path, '../' + filename)
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config
        except JSONDecodeError as e:
            print('There was a problem with parsing your config file.',
                  'Check your config.json for errors or use the config from config-example.json.')
            return
        except FileNotFoundError as e:
            print('Couldn\'t load config file. Did you create config.json in project root?')
            sys.exit(1)
        except Exception as e:
            print(type(e).__name__, e)
            sys.exit(1)

    def is_valid(self):
        grid_size = self.validate_grid_size(self.data)
        players = self.validate_players(self.data)
        chars = self.validate_player_chars(players)
        ai_settings = self.validate_ai_settings(players)
        if grid_size and players and chars and ai_settings:
            return True

    def validate_grid_size(self, config):
        try:
            # Check if grid size can be converted to int or raise ValueError.
            grid_size = int(config['grid']['size'])
            # Check if grid size is between 3 and 10 or exit.
            if 3 <= grid_size <= 10:
                return grid_size
            else:
                print('Grid size must be between 3 and 10.')
                sys.exit(1)
        except KeyError as e:
            print(type(e).__name__, 'Couldn\'t find value for grid', e, 'in your config file.' )
            sys.exit(1)
        except ValueError as e:
            print(type(e).__name__, 'Grid size must be a number.')
            sys.exit(1)
        except Exception as e:
            print(type(e).__name__, e)
            sys.exit(1)  

    def validate_players(self, config):
        try:
            # Create a list of players from the config dictionary.
            players = [ config['players'][player] for player in config['players'] ]
            # Validate for minimum number of players.
            if len(players) < 2:
                print('You need at least two players to play the game.')
                sys.exit(1)
            return players
        except Exception as e: 
            print(type(e).__name__, e)
            sys.exit(1)         

    def validate_player_chars(self, players):
        try:
            # Create a list of chars from the players dictionary.
            chars = [ player['char'].strip() for player in players ]
            # Strip is used to avoid whitespaces being counted as characters.

            for char in chars:
                # Exit program if player's char is not a single character.
                if len(char) != 1:
                    print('A player character needs to be a single character.')
                    sys.exit(1)
            # Exit program if there are duplicate chars between players.
            if len(chars) != len(set(chars)):
                print('Characters need to be unique between players.')
                sys.exit(1)
            return chars
        except KeyError as e:
            print('Couldn\'t find value for player', e, 'in your config file.' )
            sys.exit(1)
        except Exception as e:
            print(type(e).__name__, e)
            sys.exit(1)

    def validate_ai_settings(self, players):
        try:
            # Create a list of `ai` values from the players dictionary.
            ai_settings = [ player['ai'] for player in players ]
            # Make sure all `ai` values were properly converted into booleans.
            for setting in ai_settings:
                if type(setting) != bool:
                    print('If present, player AI setting needs to be either true or false.')
                    sys.exit(1)
            return ai_settings
        except KeyError as e:
            # Ignore exception to allow a player without 'ai' field
            return True
        except Exception as e:
            print(type(e).__name__, e)
            sys.exit(1)
