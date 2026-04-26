class HintEngine:

    ROW_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def __init__(self, attempt_grid, solution_grid):
        self._attempt = attempt_grid
        self._solution = solution_grid

    def get_hint(self) -> str:
        for row in self.ROW_LABELS:
            for col in range(1, 10):
                cell = self._attempt.get_cell(row, col)
                if cell.is_empty():
                    value = self._solution.get_cell(row, col).get_value()
                    return f"Hint: Cell {row}{col} = {value}"
        return "No hints available — the board is complete."
