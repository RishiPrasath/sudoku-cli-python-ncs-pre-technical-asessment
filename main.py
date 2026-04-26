from sudoku.grid import Grid
from sudoku.board_renderer import BoardRenderer
from sudoku.validator import Validator
from sudoku.hint_engine import HintEngine
from sudoku.input_parser import InputParser
from sudoku.game import Game
from constants.puzzle_data import PUZZLE, SOLUTION


def main():
    attempt_grid = Grid(PUZZLE)
    solution_grid = Grid(SOLUTION)
    renderer = BoardRenderer()
    validator = Validator()
    hint_engine = HintEngine(attempt_grid, solution_grid)
    parser = InputParser()

    game = Game(attempt_grid, solution_grid, renderer, validator, hint_engine, parser)
    game.run()


if __name__ == "__main__":
    main()
