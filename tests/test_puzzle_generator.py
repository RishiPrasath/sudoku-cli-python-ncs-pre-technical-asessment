import pytest
from sudoku.puzzle_generator import PuzzleGenerator


def test_generated_solution_is_fully_filled():
    # Arrange + Act
    _, solution = PuzzleGenerator().generate()
    # Assert
    assert all(solution[r][c] != 0 for r in range(9) for c in range(9))


def test_generated_puzzle_has_30_clues():
    # Arrange + Act
    puzzle, _ = PuzzleGenerator().generate()
    # Assert
    clues = sum(1 for r in range(9) for c in range(9) if puzzle[r][c] != 0)
    assert clues == 30


def test_puzzle_clues_match_solution():
    # Arrange + Act
    puzzle, solution = PuzzleGenerator().generate()
    # Assert
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                assert puzzle[r][c] == solution[r][c]


def test_generated_solution_has_no_row_duplicates():
    # Arrange + Act
    _, solution = PuzzleGenerator().generate()
    # Assert
    for row in solution:
        assert sorted(row) == list(range(1, 10))


def test_generated_solution_has_no_column_duplicates():
    # Arrange + Act
    _, solution = PuzzleGenerator().generate()
    # Assert
    for c in range(9):
        col = [solution[r][c] for r in range(9)]
        assert sorted(col) == list(range(1, 10))


def test_generated_solution_has_no_subgrid_duplicates():
    # Arrange + Act
    _, solution = PuzzleGenerator().generate()
    # Assert
    for box_r in range(3):
        for box_c in range(3):
            vals = [
                solution[box_r * 3 + r][box_c * 3 + c]
                for r in range(3)
                for c in range(3)
            ]
            assert sorted(vals) == list(range(1, 10))


def test_consecutive_calls_produce_different_puzzles():
    # Arrange + Act
    puzzle1, _ = PuzzleGenerator().generate()
    puzzle2, _ = PuzzleGenerator().generate()
    # Assert
    assert puzzle1 != puzzle2
