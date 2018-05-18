from tictactoe import Game, GameConfig

def main(args=None):
    """Main program routine."""    
    print("=======================\nTic-Tac-Toe: Remastered\n=======================")

    config = GameConfig('config.json')  
    # Note that config.json is exptected to be found in project root.

    if config.is_valid():
        # Intialize Game instance when we are sure the config is valid.
        game = Game(config)
        game.run()

if __name__ == '__main__':
    main()
