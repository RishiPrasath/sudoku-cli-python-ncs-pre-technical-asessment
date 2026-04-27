import random
import copy


class SolutionGenerator:

    def generate(self):
        grid = [[0] * 9 for _ in range(9)]
        self._fill(grid, 0)
        return grid

    def _fill(self, grid, pos):
        if pos == 81:
            return True
        row, col = divmod(pos, 9)
        candidates = list(range(1, 10))
        random.shuffle(candidates)
        for num in candidates:
            if self._is_valid(grid, row, col, num):
                grid[row][col] = num
                if self._fill(grid, pos + 1):
                    return True
                grid[row][col] = 0
        return False

    def _is_valid(self, grid, row, col, num):
        if num in grid[row]:
            return False
        if any(grid[r][col] == num for r in range(9)):
            return False
        box_r, box_c = (row // 3) * 3, (col // 3) * 3
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if grid[r][c] == num:
                    return False
        return True


class PuzzleCarver:

    TARGET_CLUES = 30

    def carve(self, solution):
        puzzle = copy.deepcopy(solution)
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        removed = 0
        target = 81 - self.TARGET_CLUES
        for row, col in cells:
            if removed == target:
                break
            backup = puzzle[row][col]
            puzzle[row][col] = 0
            if self._has_unique_solution(puzzle):
                removed += 1
            else:
                puzzle[row][col] = backup
        return puzzle

    def _has_unique_solution(self, grid):
        work = copy.deepcopy(grid)
        count = [0]
        self._solve(work, 0, count)
        return count[0] == 1

    def _solve(self, grid, pos, count):
        if count[0] > 1:
            return
        if pos == 81:
            count[0] += 1
            return
        row, col = divmod(pos, 9)
        if grid[row][col] != 0:
            self._solve(grid, pos + 1, count)
            return
        for num in range(1, 10):
            if self._is_valid(grid, row, col, num):
                grid[row][col] = num
                self._solve(grid, pos + 1, count)
                grid[row][col] = 0
                if count[0] > 1:
                    return

    def _is_valid(self, grid, row, col, num):
        if num in grid[row]:
            return False
        if any(grid[r][col] == num for r in range(9)):
            return False
        box_r, box_c = (row // 3) * 3, (col // 3) * 3
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if grid[r][c] == num:
                    return False
        return True


class PuzzleGenerator:

    def __init__(self):
        self._solution_gen = SolutionGenerator()
        self._carver = PuzzleCarver()

    def generate(self):
        solution = self._solution_gen.generate()
        puzzle = self._carver.carve(solution)
        return puzzle, solution
