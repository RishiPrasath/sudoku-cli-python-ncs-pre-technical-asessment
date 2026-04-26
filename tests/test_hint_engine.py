import pytest
from sudoku.grid import Grid
from sudoku.hint_engine import HintEngine
from constants.puzzle_data import PUZZLE, SOLUTION


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
