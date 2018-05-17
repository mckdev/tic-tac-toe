import pytest
import re

from tictactoe import Grid, Player


class TestPlayer:
    """Tests methods of tictactoe.player.Player class."""

    def test_player_init(self):
        """Test Player initialization."""
        config = {'char': 'X', 'ai': False}
        player = Player(config)
        assert player.char is 'X' and player.ai is False

        config = {'char': '@', 'ai': True}
        player = Player(config)
        assert player.char is '@' and player.ai is True

    def test_player_move(self, monkeypatch):
        """Test Player.move method."""
        config = {'char': 'X', 'ai': False}
        player = Player(config)
        # Monkeypatch Python's input function for this test's runtime.
        monkeypatch.setattr('builtins.input', lambda: 'test input')
        i = player.move()
        assert i == ('test input')

    def test_ai_move(self):
        """Test Player.ai_move method."""
        config = {'char': '@', 'ai': True}
        player = Player(config)
        grid = Grid(3)
        i = player.ai_move(grid)
        # Assert AI input is in correct format.
        assert re.match(r'^\d\,\d$', i)
        # Assert AI input is within the grid.
        i = i.split(',')
        x = int(i[0])
        y = int(i[1])
        assert 0 <= x <= grid.size
        assert 0 <= y <= grid.size
