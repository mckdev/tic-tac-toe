from .config import GameConfig
from .game import Game
from .grid import Grid
from .player import Player
from .referee import Referee


def run():
    print("=======================\nTic-Tac-Toe: Remastered\n=======================")

    config = GameConfig('config.json')

    if config.is_valid():
        game = Game(config)
        game.run()
