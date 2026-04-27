import pytest
from sudoku.grid import Grid
from sudoku.validator import Validator

PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

SOLUTION = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def test_validator_clean_partial_grid_returns_none():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Assert
    assert validator.check(grid) is None


def test_validator_complete_valid_grid_returns_none():
    # Arrange
    grid = Grid(SOLUTION)
    validator = Validator()
    # Assert
    assert validator.check(grid) is None


def test_validator_row_duplicate_detected():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — place a 3 in A3 (Row A already has a 3 at A2)
    grid.set_cell("A", 3, 3)
    result = validator.check(grid)
    # Assert
    assert result == "Number 3 already exists in Row A."


def test_validator_column_duplicate_detected():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — place a 5 in B1 (Col 1 already has a 5 via Row A col 1)
    grid.set_cell("B", 3, 6)
    grid.set_cell("D", 2, 5)
    # Col 2 has 3 and 9 — place another 9 in D2 would conflict
    grid2 = Grid(PUZZLE)
    grid2.set_cell("D", 2, 9)
    result = validator.check(grid2)
    # Assert
    assert result == "Number 9 already exists in Column 2."


def test_validator_zone_duplicate_detected():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — Zone top-left has 9 at C2, place another 9 in A3 (col 3 has no 9)
    grid.set_cell("A", 3, 9)
    result = validator.check(grid)
    # Assert
    assert result == "Number 9 already exists in the same 3×3 subgrid."


def test_validator_empty_cells_ignored():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Assert — partial grid with empty cells should be clean
    assert validator.check(grid) is None


def test_validator_multiple_violations_returns_first():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — create row violation first (rows checked before cols)
    grid.set_cell("A", 3, 3)
    result = validator.check(grid)
    # Assert — should return row violation, not col or zone
    assert "Row A" in result


def test_validator_prefilled_cells_included_in_check():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — Row A has pre-filled 5 at A1, place another 5 in A3
    grid.set_cell("A", 3, 5)
    result = validator.check(grid)
    # Assert
    assert result == "Number 5 already exists in Row A."


def test_validator_spec_example_place_a3_equals_3():
    # Arrange
    grid = Grid(PUZZLE)
    validator = Validator()
    # Act — Row A already has 3 at A2, placing 3 at A3 violates row
    grid.set_cell("A", 3, 3)
    result = validator.check(grid)
    # Assert
    assert result == "Number 3 already exists in Row A."
