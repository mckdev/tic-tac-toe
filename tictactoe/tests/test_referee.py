import pytest

from tictactoe import Game, GameConfig, Grid, Referee


@pytest.fixture()
def game():
    config = GameConfig('config_example.json')
    game = Game(config)
    yield game


@pytest.fixture()
def referee(game):
    referee = Referee(game)
    yield referee


class TestReferee:
    """Tests tictactoe.referee.Referee class methods."""

    def test_referee_init(self, referee, game):
        """Test Referee initialization."""
        assert isinstance(referee, Referee)
        assert isinstance(referee.game, Game) and referee.game == game
        assert isinstance(referee.grid, Grid) and referee.grid == game.grid

    def test_referee_input_validation(self, capsys, game, referee):
        """Test referee.validate_input method."""
        player = game.players[0]

        # Test few invalid inputs
        referee.validate_input('asdf', player)
        captured = capsys.readouterr()
        assert 'You must provide input in "<row>,<col>" format' in captured.out

        referee.validate_input('s,s', player)
        captured = capsys.readouterr()
        assert 'You must provide input in "<row>,<col>" format' in captured.out

        referee.validate_input('1,1,1', player)
        captured = capsys.readouterr()
        assert 'You must provide input in "<row>,<col>" format' in captured.out           

        referee.validate_input('10,10', player)
        captured = capsys.readouterr()
        assert 'You must provide input in "<row>,<col>" format' in captured.out

        # Test input out of range
        referee.validate_input('9,9', player)
        captured = capsys.readouterr()
        assert 'You must provide values which fit on the grid' in captured.out

        # Test valid input
        referee.validate_input('1,1', player)
        captured = capsys.readouterr()
        assert 'OK!' in captured.out

        # Test position taken
        game.grid.update(1,1,'X')
        referee.validate_input('1,1', player)
        captured = capsys.readouterr()
        assert 'This position is already taken' in captured.out

    def test_referee_input_processing(self, referee):
        """Test Referee.process_input method."""
        assert referee.process_input('2, 1') == (2, 1)
        assert referee.process_input('5,5') == (5, 5)

    def test_referee_check_for_winner(self, capsys, referee):
        """Test Referee.check_for_winner method."""

        # Diagonal 1
        referee.grid.data = [
            ['X','Y','V'],
            ['V','X','Y'],
            ['X','Y','X']
        ]
        with pytest.raises(SystemExit):
            assert referee.check_for_winner()
        captured = capsys.readouterr()
        assert 'X IS THE WINNER' in captured.out
        
        # Diagonal 2
        referee.grid.data = [
            ['X','Y','V'],
            ['V','V','Y'],
            ['V','Y','X']
        ]
        with pytest.raises(SystemExit):
            assert referee.check_for_winner()
        captured = capsys.readouterr()
        assert 'V IS THE WINNER' in captured.out

        # Horizontal
        referee.grid.data = [
            ['X','Y','V'],
            ['O','O','O'],
            ['V','Y','X']
        ]
        with pytest.raises(SystemExit):
            assert referee.check_for_winner()
        captured = capsys.readouterr()
        assert 'O IS THE WINNER' in captured.out             

        # Vertical
        referee.grid.data = [
            ['X','@','V'],
            ['O','@','O'],
            ['V','@','X']
        ]
        with pytest.raises(SystemExit):
            assert referee.check_for_winner()
        captured = capsys.readouterr()
        assert '@ IS THE WINNER' in captured.out

    def test_referee_check_for_full_grid(self, capsys, referee):
        """Tests Referee.check_for_full_grid method"""
        referee.grid.data = [
            ['X','Y','V'],
            ['V','X','Y'],
            ['X','Y','V']
        ]
        with pytest.raises(SystemExit):
            assert referee.check_for_full_grid()
        captured = capsys.readouterr()        
        assert 'Grid full' in captured.out
