# Sudoku — Command Line Game

A command-line Sudoku game built in Python.

---

## Environment

- **OS:** Windows, macOS, or Linux
- **Python:** 3.10 or higher (tested on Python 3.12 and 3.14)
- **Dependencies:** pytest (for running tests only) — no external libraries required to play

---

## How to Run

**Windows:**

```
cd code
venv\Scripts\activate
python main.py
```

**macOS / Linux:**

```
cd code
source venv/bin/activate
python main.py
```

If you do not want to use the virtual environment, ensure Python 3.10+ is installed and run:

```
python main.py
```

---

## How to Run Tests

```
cd code
venv\Scripts\activate
pytest tests/ -v
```

**77 tests across 8 test files — all passing.**

---

## Commands

CommandExampleDescriptionPlace a number`A3 4`Place value 4 at row A, column 3Clear a cell`C5 clear`Clear a player-placed valueGet a hint`hint`Reveals the correct value for the first empty cellCheck for violations`check`Checks all rows, columns and 3×3 subgrids for duplicatesQuit`quit`Exit the game

---

## Rules

- Rows are labelled A to I (top to bottom)
- Columns are numbered 1 to 9 (left to right)
- Valid values are integers 1 to 9
- Pre-filled cells cannot be changed or cleared
- No number may repeat in any row, column, or 3×3 subgrid

---

## Design and Assumptions

### Architecture

The game is built around 9 classes, each with a single responsibility:

- **Cell** — represents one square on the board. Owns its value and pre-filled status. Enforces all placement rules (value must be 1–9, pre-filled cells are immutable).
- **Grid** — holds 81 Cell objects in a 9×9 structure. Provides access by row letter and column number. Translates between the player's coordinate system (A–I, 1–9) and internal list indexes.
- **BoardRenderer** — reads the Grid and prints the board to the terminal in the spec format.
- **Validator** — checks the Grid for rule violations. Scans rows, then columns, then 3×3 subgrids. Returns the first violation found, or None if the board is clean.
- **InputParser** — parses raw text typed by the player into a structured command dictionary. Returns None for any unrecognised or malformed input.
- **PuzzleGenerator** — generates a random, valid Sudoku puzzle on each run. Uses a backtracking algorithm to produce a complete solution, then carves cells to create a puzzle with a unique solution (~30 clues).
- **HintEngine** — scans the attempt grid for the first empty cell and returns the correct value from the solution grid.
- **Game** — orchestrates the game loop. Receives a parsed command and delegates to the correct class. Checks the win condition after every valid placement.
- [**main.py**](http://main.py) — entry point. Creates all objects and starts the game.

### Assumptions

- A new puzzle is randomly generated each time the game starts. The generator produces a complete valid solution, then removes cells while ensuring the puzzle has exactly one solution.
- The solution grid is created once at startup and never modified. Only the attempt grid changes.
- The hint command always reveals the first empty cell in row-major order (A1 → A2 → ... → I9).
- The check command reports the first violation found — row violations take priority over column violations, which take priority over subgrid violations.
- Placing a value on a cell that already has a player-placed value overwrites it (the cell is not pre-filled, so the move is valid).
- The win condition requires all 81 cells to be filled and no rule violations to exist.

### SOLID Principles Applied

- **Single Responsibility** — each class has one job and owns only the data it needs
- **Open/Closed** — new commands can be added to Game without modifying existing classes
- **Dependency Inversion** — Game receives its dependencies (validator, renderer, etc.) via constructor injection, not hard-coded imports

### Testing Approach

All classes were built using Test-Driven Development (TDD) — tests were written first, then the implementation was written to make them pass. Each test file covers one class.

---

## Project Structure

```
code/
├── main.py                        # Entry point
├── requirements.txt               # pytest dependency
├── sudoku/
│   ├── cell.py                    # One square on the board
│   ├── grid.py                    # 9×9 board of Cell objects
│   ├── board_renderer.py          # Prints the board to terminal
│   ├── validator.py               # Checks rows, columns, subgrids
│   ├── input_parser.py            # Parses raw player input
│   ├── hint_engine.py             # Reveals correct value for first empty cell
│   ├── puzzle_generator.py        # Generates random puzzles with unique solutions
│   └── game.py                    # Game loop and command orchestration
└── tests/
    ├── test_cell.py               # 10 tests
    ├── test_grid.py               # 16 tests
    ├── test_board_renderer.py     # 4 tests
    ├── test_validator.py          # 9 tests
    ├── test_input_parser.py       # 16 tests
    ├── test_hint_engine.py        # 4 tests
    ├── test_puzzle_generator.py   # 7 tests
    └── test_game.py               # 11 tests
```
