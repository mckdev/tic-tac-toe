import pytest

from tictactoe import Game, GameConfig, Grid, Referee


class TestGame:
    """Tests tictactoe.referee.Game class methods."""
    
    def test_game_initiation(self):
        """Tests game initiation with example config."""
        config = GameConfig('config_example.json')
        game = Game(config)

        # Assert grid was initiated according to config.
        assert isinstance(game.grid, Grid) and game.grid.size == config['grid']['size']
        # Assert list of players were initiated according to config.
        assert isinstance(game.players, list) and len(game.players) == len(config['players'])
        # Assert referee was initiated.
        assert isinstance(game.referee, Referee)

        game.init_referee()

    def test_game_run_with_ai(self, capsys):
        """Tests game run with 3 AI players and no human players."""
        config = GameConfig('tictactoe/tests/configs/config_with_3_ai.json')
        game = Game(config)


        with pytest.raises(SystemExit):     
            game.run()
        captured = capsys.readouterr()

        # Assert game finished successfully and correct message is displayed.
        assert "Game finished" in captured.out and str(game.completed_turns) in captured.out
