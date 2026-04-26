import pytest
from sudoku.grid import Grid
from sudoku.board_renderer import BoardRenderer
from constants.puzzle_data import PUZZLE


def test_board_renderer_output_contains_column_header():
    # Arrange
    grid = Grid(PUZZLE)
    renderer = BoardRenderer()
    # Act
    output = renderer.render(grid)
    # Assert
    assert "1 2 3 4 5 6 7 8 9" in output


def test_board_renderer_output_contains_row_a_label_and_values():
    # Arrange
    grid = Grid(PUZZLE)
    renderer = BoardRenderer()
    # Act
    output = renderer.render(grid)
    # Assert
    assert "A" in output
    assert "5" in output
    assert "3" in output


def test_board_renderer_shows_underscore_for_empty_cells():
    # Arrange
    grid = Grid(PUZZLE)
    renderer = BoardRenderer()
    # Act
    output = renderer.render(grid)
    # Assert
    assert "_" in output


def test_board_renderer_row_format_matches_spec():
    # Arrange
    grid = Grid(PUZZLE)
    renderer = BoardRenderer()
    # Act
    output = renderer.render(grid)
    # Assert — Row A must appear as "  A 5 3 _ ..."
    assert "  A 5 3 _" in output
