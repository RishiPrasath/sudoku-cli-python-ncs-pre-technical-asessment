import pytest
from sudoku.grid import Grid
from sudoku.hint_engine import HintEngine

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


def test_hint_engine_returns_hint_string_on_partial_grid():
    # Arrange
    attempt_grid = Grid(PUZZLE)
    solution_grid = Grid(SOLUTION)
    engine = HintEngine(attempt_grid, solution_grid)
    # Act
    result = engine.get_hint()
    # Assert
    assert result.startswith("Hint: Cell")


def test_hint_engine_revealed_value_matches_solution():
    # Arrange
    attempt_grid = Grid(PUZZLE)
    solution_grid = Grid(SOLUTION)
    engine = HintEngine(attempt_grid, solution_grid)
    # Act
    result = engine.get_hint()
    # Assert — parse the hint and verify value matches solution
    # Format: "Hint: Cell A3 = 4"
    parts = result.split()
    cell_ref = parts[2]  # e.g. "A3"
    value = int(parts[4])  # e.g. 4
    row = cell_ref[0]
    col = int(cell_ref[1])
    assert solution_grid.get_cell(row, col).get_value() == value


def test_hint_engine_output_format_exact():
    # Arrange
    attempt_grid = Grid(PUZZLE)
    solution_grid = Grid(SOLUTION)
    engine = HintEngine(attempt_grid, solution_grid)
    # Act
    result = engine.get_hint()
    # Assert — must match "Hint: Cell XN = V" exactly
    parts = result.split()
    assert len(parts) == 5
    assert parts[0] == "Hint:"
    assert parts[1] == "Cell"
    assert parts[3] == "="
    assert parts[4].isdigit()


def test_hint_engine_full_grid_returns_no_hints_message():
    # Arrange
    attempt_grid = Grid(SOLUTION)
    solution_grid = Grid(SOLUTION)
    engine = HintEngine(attempt_grid, solution_grid)
    # Act
    result = engine.get_hint()
    # Assert
    assert result == "No hints available — the board is complete."
