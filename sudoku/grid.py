from sudoku.cell import Cell


class Grid:

    ROW_MAP = {
        "A": 0, "B": 1, "C": 2,
        "D": 3, "E": 4, "F": 5,
        "G": 6, "H": 7, "I": 8,
    }

    def __init__(self, data):
        self._cells = []
        for row in data:
            cell_row = []
            for val in row:
                if val == 0:
                    cell_row.append(Cell())
                else:
                    cell_row.append(Cell(value=val, is_prefilled=True))
            self._cells.append(cell_row)

    def _get_indexes(self, row, col):
        if row not in self.ROW_MAP:
            raise ValueError(f"Invalid row: {row}. Must be A-I.")
        return self.ROW_MAP[row], col - 1

    def get_cell(self, row, col):
        r, c = self._get_indexes(row, col)
        return self._cells[r][c]

    def set_cell(self, row, col, value):
        self.get_cell(row, col).set_value(value)

    def clear_cell(self, row, col):
        self.get_cell(row, col).clear()

    def is_complete(self):
        return all(
            not self._cells[r][c].is_empty()
            for r in range(9)
            for c in range(9)
        )

    def get_row_cells(self, row):
        r = self.ROW_MAP[row]
        return self._cells[r]

    def get_col_cells(self, col):
        c = col - 1
        return [self._cells[r][c] for r in range(9)]

    def get_zone_cells(self, zone_row, zone_col):
        cells = []
        for r in range(zone_row * 3, zone_row * 3 + 3):
            for c in range(zone_col * 3, zone_col * 3 + 3):
                cells.append(self._cells[r][c])
        return cells
