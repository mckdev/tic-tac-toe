import pytest

from tictactoe import Grid

class TestGrid:
    """Tests methods of tictactoe.grid.Grid class."""

    def test_grid_init(self):
        """Test Grid initialization."""
        grid = Grid(10)
        assert isinstance(grid, Grid)
        assert isinstance(grid.data, list)
        assert grid.size == 10

    def test_full_grid(self):
        """Tests Grid.is_full method."""
        grid = Grid(3)

        # Test full grid
        grid.data = [
            ['X','Y','V'],
            ['V','X','Y'],
            ['X','Y','V']
        ]
        assert grid.is_full()

        # Test not full grid
        grid.data = [
            ['(0,1)','Y','V'],
            ['V','X','Y'],
            ['X','Y','V']
        ]
        assert not grid.is_full()

    def test_grid_is_occupied(self):
        """Tests Grid.is_occupied method."""
        grid = Grid(3)
        grid.data[0][2] = 'X'
        # Test occupied position
        assert grid.is_occupied(0,2)
        # Test free position
        assert not grid.is_occupied(0,1)          

    def test_grid_display(self, capsys):
        """Test output of Grid.show method."""
        grid = Grid(3)
        grid.data = [
            ['X','Y','V'],
            ['V','X','Y'],
            ['X','Y','X']
        ]
        grid.show()
        captured = capsys.readouterr()
        # Test for expected output of the core part of the grid
        assert '0\t    1\t    2\t' in captured.out
        assert '\r\n\t ------------------------\n' in captured.out
        assert '------------------------\n\r\n' in captured.out

    def test_grid_flat(self, capsys):
        """Test output of Grid.flat method."""
        grid = Grid(3)
        # Assert that flattened grid is a list with length of grid size squared
        assert isinstance(grid.flat(), list) and len(grid.flat()) == grid.size ** 2

    def test_grid_update(self, capsys):
        """Test Grid.update method."""
        grid = Grid(3)
        grid.update(1,1,'x')
        assert 'x' in grid[1][1]
        grid.update(2,0,'y')
        assert 'y' in grid[2][0]
