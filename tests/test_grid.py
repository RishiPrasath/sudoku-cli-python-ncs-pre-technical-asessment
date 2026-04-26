import pytest
from sudoku.grid import Grid
from constants.puzzle_data import PUZZLE, SOLUTION


def test_grid_has_81_cells():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    total = sum(1 for r in range(9) for c in range(9))
    assert total == 81


def test_grid_has_30_prefilled_cells():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    prefilled = sum(1 for r in "ABCDEFGHI" for c in range(1, 10) if grid.get_cell(r, c).is_prefilled())
    assert prefilled == 30


def test_grid_has_51_empty_cells():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    empty = sum(1 for r in "ABCDEFGHI" for c in range(1, 10) if grid.get_cell(r, c).is_empty())
    assert empty == 51


def test_grid_get_cell_returns_correct_prefilled_value():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert grid.get_cell("A", 1).get_value() == 5
    assert grid.get_cell("A", 1).is_prefilled() == True


def test_grid_get_cell_returns_empty_cell():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert grid.get_cell("A", 3).is_empty() == True


def test_grid_set_cell_updates_value():
    # Arrange
    grid = Grid(PUZZLE)
    # Act
    grid.set_cell("A", 3, 4)
    # Assert
    assert grid.get_cell("A", 3).get_value() == 4


def test_grid_clear_cell_empties_value():
    # Arrange
    grid = Grid(PUZZLE)
    grid.set_cell("A", 3, 4)
    # Act
    grid.clear_cell("A", 3)
    # Assert
    assert grid.get_cell("A", 3).is_empty() == True


def test_grid_is_complete_returns_false_on_partial():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert grid.is_complete() == False


def test_grid_is_complete_returns_true_when_full():
    # Arrange
    grid = Grid(SOLUTION)
    # Assert
    assert grid.is_complete() == True


def test_grid_get_row_cells_returns_9_cells():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert len(grid.get_row_cells("A")) == 9


def test_grid_get_col_cells_returns_9_cells():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert len(grid.get_col_cells(1)) == 9


def test_grid_get_zone_cells_returns_9_cells_zone_1():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    assert len(grid.get_zone_cells(0, 0)) == 9


def test_grid_get_zone_cells_returns_correct_cells_zone_5():
    # Arrange
    grid = Grid(PUZZLE)
    # Assert
    cells = grid.get_zone_cells(1, 1)
    values = [c.get_value() for c in cells]
    assert len(cells) == 9


def test_grid_get_cell_raises_on_invalid_row():
    # Arrange
    grid = Grid(PUZZLE)
    # Act + Assert
    with pytest.raises(ValueError):
        grid.get_cell("Z", 1)


def test_grid_set_cell_raises_on_prefilled():
    # Arrange
    grid = Grid(PUZZLE)
    # Act + Assert
    with pytest.raises(ValueError):
        grid.set_cell("A", 1, 9)


def test_grid_clear_cell_raises_on_prefilled():
    # Arrange
    grid = Grid(PUZZLE)
    # Act + Assert
    with pytest.raises(ValueError):
        grid.clear_cell("A", 1)
