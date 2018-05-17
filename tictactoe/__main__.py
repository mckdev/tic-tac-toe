from tictactoe import Game, GameConfig

def main(args=None):
    print("=======================\nTic-Tac-Toe: Remastered\n=======================")

    config = GameConfig('config.json')

    if config.is_valid():
        game = Game(config)
        game.run()

if __name__ == '__main__':
    main()
