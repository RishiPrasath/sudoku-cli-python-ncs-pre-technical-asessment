"""
puzzle_data.py

Hardcoded puzzle constants for the NCS Sudoku assignment.
Source: problem specification (ADR-008).

PUZZLE  — the starting board. 0 represents an empty cell.
SOLUTION — the fully completed board. Used by HintEngine to reveal correct values.
"""

PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],  # Row A
    [6, 0, 0, 1, 9, 5, 0, 0, 0],  # Row B
    [0, 9, 8, 0, 0, 0, 0, 6, 0],  # Row C
    [8, 0, 0, 0, 6, 0, 0, 0, 3],  # Row D
    [4, 0, 0, 8, 0, 3, 0, 0, 1],  # Row E
    [7, 0, 0, 0, 2, 0, 0, 0, 6],  # Row F
    [0, 6, 0, 0, 0, 0, 2, 8, 0],  # Row G
    [0, 0, 0, 4, 1, 9, 0, 0, 5],  # Row H
    [0, 0, 0, 0, 8, 0, 0, 7, 9],  # Row I
]

SOLUTION = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],  # Row A
    [6, 7, 2, 1, 9, 5, 3, 4, 8],  # Row B
    [1, 9, 8, 3, 4, 2, 5, 6, 7],  # Row C
    [8, 5, 9, 7, 6, 1, 4, 2, 3],  # Row D
    [4, 2, 6, 8, 5, 3, 7, 9, 1],  # Row E
    [7, 1, 3, 9, 2, 4, 8, 5, 6],  # Row F
    [9, 6, 1, 5, 3, 7, 2, 8, 4],  # Row G
    [2, 8, 7, 4, 1, 9, 6, 3, 5],  # Row H
    [3, 4, 5, 2, 8, 6, 1, 7, 9],  # Row I
]