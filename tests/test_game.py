import pytest
from unittest.mock import patch
from sudoku.grid import Grid
from sudoku.game import Game
from sudoku.board_renderer import BoardRenderer
from sudoku.validator import Validator
from sudoku.hint_engine import HintEngine
from sudoku.input_parser import InputParser

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


def make_game():
    attempt = Grid(PUZZLE)
    solution = Grid(SOLUTION)
    renderer = BoardRenderer()
    validator = Validator()
    hint_engine = HintEngine(attempt, solution)
    parser = InputParser()
    return Game(attempt, solution, renderer, validator, hint_engine, parser)


def test_game_place_valid_move_accepted():
    # Arrange
    game = make_game()
    # Act
    result = game._place("A", 3, 4)
    # Assert
    assert result == "Move accepted."
    assert game._attempt.get_cell("A", 3).get_value() == 4


def test_game_place_on_prefilled_cell_rejected():
    # Arrange
    game = make_game()
    # Act
    result = game._place("A", 1, 9)
    # Assert
    assert result == "Invalid move. A1 is pre-filled."


def test_game_clear_user_filled_cell():
    # Arrange
    game = make_game()
    game._place("A", 3, 4)
    # Act
    result = game._clear("A", 3)
    # Assert
    assert result == "Cell A3 cleared."
    assert game._attempt.get_cell("A", 3).is_empty()


def test_game_check_clean_board_returns_no_violations():
    # Arrange
    game = make_game()
    # Act
    result = game._check()
    # Assert
    assert result == "No rule violations detected."


def test_game_check_with_row_violation():
    # Arrange
    game = make_game()
    game._attempt.set_cell("A", 3, 3)
    # Act
    result = game._check()
    # Assert
    assert "Row A" in result


def test_game_check_with_column_violation():
    # Arrange
    game = make_game()
    game._attempt.set_cell("D", 2, 9)
    # Act
    result = game._check()
    # Assert
    assert "Column" in result


def test_game_check_with_subgrid_violation():
    # Arrange
    game = make_game()
    game._attempt.set_cell("A", 3, 9)
    # Act
    result = game._check()
    # Assert
    assert "3×3 subgrid" in result or "subgrid" in result


def test_game_hint_returns_hint_string():
    # Arrange
    game = make_game()
    # Act
    result = game._hint()
    # Assert
    assert result.startswith("Hint: Cell")


def test_game_check_win_returns_false_on_partial():
    # Arrange
    game = make_game()
    # Assert
    assert game._check_win() == False


def test_game_check_win_returns_true_when_complete():
    # Arrange
    attempt = Grid(SOLUTION)
    solution = Grid(SOLUTION)
    game = Game(attempt, solution, BoardRenderer(), Validator(),
                HintEngine(attempt, solution), InputParser())
    # Assert
    assert game._check_win() == True


def test_game_place_invalid_value_rejected():
    # Arrange
    game = make_game()
    # Act — try to place value 10 (out of range)
    result = game._place("A", 3, 10)
    # Assert
    assert "Invalid" in result
