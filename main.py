from sudoku.grid import Grid
from sudoku.board_renderer import BoardRenderer
from sudoku.validator import Validator
from sudoku.hint_engine import HintEngine
from sudoku.input_parser import InputParser
from sudoku.game import Game
from sudoku.puzzle_generator import PuzzleGenerator


def main():
    puzzle_2d, solution_2d = PuzzleGenerator().generate()
    attempt_grid = Grid(puzzle_2d)
    solution_grid = Grid(solution_2d)
    renderer = BoardRenderer()
    validator = Validator()
    hint_engine = HintEngine(attempt_grid, solution_grid)
    parser = InputParser()

    game = Game(attempt_grid, solution_grid, renderer, validator, hint_engine, parser)
    game.run()


if __name__ == "__main__":
    main()
