import pytest
from sudoku.input_parser import InputParser


def test_input_parser_place_command():
    # Arrange
    parser = InputParser()
    # Act
    result = parser.parse("A3 4")
    # Assert
    assert result == {"type": "place", "row": "A", "col": 3, "value": 4}


def test_input_parser_clear_command():
    # Arrange
    parser = InputParser()
    # Act
    result = parser.parse("C5 clear")
    # Assert
    assert result == {"type": "clear", "row": "C", "col": 5}


def test_input_parser_hint_command():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("hint") == {"type": "hint"}


def test_input_parser_check_command():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("check") == {"type": "check"}


def test_input_parser_quit_command():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("quit") == {"type": "quit"}


def test_input_parser_lowercase_row_handled():
    # Arrange
    parser = InputParser()
    # Act
    result = parser.parse("a3 4")
    # Assert
    assert result == {"type": "place", "row": "A", "col": 3, "value": 4}


def test_input_parser_uppercase_command_handled():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("HINT") == {"type": "hint"}


def test_input_parser_extra_whitespace_handled():
    # Arrange
    parser = InputParser()
    # Act
    result = parser.parse("  A3 4  ")
    # Assert
    assert result["type"] == "place"


def test_input_parser_invalid_row_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("Z3 4") is None


def test_input_parser_col_zero_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("A0 4") is None


def test_input_parser_col_ten_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("A10 4") is None


def test_input_parser_value_zero_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("A3 0") is None


def test_input_parser_value_ten_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("A3 10") is None


def test_input_parser_empty_string_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("") is None


def test_input_parser_unrecognised_input_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("hello") is None


def test_input_parser_missing_value_returns_none():
    # Arrange
    parser = InputParser()
    # Act + Assert
    assert parser.parse("A3") is None
