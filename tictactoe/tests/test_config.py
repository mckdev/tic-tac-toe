import pytest

from tictactoe import GameConfig


class TestConfig:
    """Tests tictactoe.config.Config class and config.json file validation."""

    def test_config_example(self):
        """Tests the example config file which should pass all validations."""
        config = GameConfig('config_example.json')
        assert config.is_valid()

    def test_config_with_error(self, capsys):
        """Tests configs with syntax errors and empty configs"""
        GameConfig('tictactoe/tests/configs/config_with_error.json')
        captured = capsys.readouterr()
        assert "There was a problem with parsing your config file." in captured.out

    def test_config_which_doesnt_exist(self, capsys):
        """Tests for non existing config paths"""
        with pytest.raises(SystemExit):
            config = GameConfig('tictactoe/tests/configs/config_which_doesnt_exist.json')
        captured = capsys.readouterr()
        assert "Couldn't load config file." in captured.out

    def test_config_with_invalid_grid(self, capsys):
        """Test for too small and too big grid sizes"""
        config = GameConfig('tictactoe/tests/configs/config_with_2x2_grid.json')
        with pytest.raises(SystemExit):
            config.validate_grid_size(config)
        captured = capsys.readouterr()
        assert "Grid size must be between 3 and 10." in captured.out

        config = GameConfig('tictactoe/tests/configs/config_with_11x11_grid.json')
        with pytest.raises(SystemExit):
            config.validate_grid_size(config)
        captured = capsys.readouterr()
        assert "Grid size must be between 3 and 10." in captured.out

    def test_config_with_invalid_char(self, capsys):
        """Tests for invalid or empty player character."""
        config = GameConfig('tictactoe/tests/configs/config_with_invalid_char.json')
        players = [ config['players'][player] for player in config['players'] ]
        with pytest.raises(SystemExit):
            config.validate_player_chars(players)
        captured = capsys.readouterr()
        assert "A player character needs to be a single character." in captured.out

    def test_config_with_duplicate_char(self, capsys):
        """Tests for duplicate player character."""
        config = GameConfig('tictactoe/tests/configs/config_with_duplicate_char.json')
        players = [ config['players'][player] for player in config['players'] ]
        with pytest.raises(SystemExit):
            config.validate_player_chars(players)
        captured = capsys.readouterr()
        assert "Characters need to be unique between players." in captured.out

    def test_config_with_invalid_ai(self, capsys):
        """Tests config for invalid AI setting."""
        config = GameConfig('tictactoe/tests/configs/config_with_invalid_ai.json')
        players = [ config['players'][player] for player in config['players'] ]
        with pytest.raises(SystemExit):
            config.validate_ai_settings(players)
        captured = capsys.readouterr()
        assert "If present, player AI setting needs to be either true or false." in captured.out
