class Validator:

    ROW_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def check(self, grid) -> str | None:
        result = self._check_rows(grid)
        if result:
            return result
        result = self._check_columns(grid)
        if result:
            return result
        result = self._check_subgrids(grid)
        if result:
            return result
        return None

    def _find_duplicate(self, cells) -> int | None:
        seen = set()
        for cell in cells:
            if not cell.is_empty():
                val = cell.get_value()
                if val in seen:
                    return val
                seen.add(val)
        return None

    def _check_rows(self, grid) -> str | None:
        for label in self.ROW_LABELS:
            cells = grid.get_row_cells(label)
            dup = self._find_duplicate(cells)
            if dup:
                return f"Number {dup} already exists in Row {label}."
        return None

    def _check_columns(self, grid) -> str | None:
        for col in range(1, 10):
            cells = grid.get_col_cells(col)
            dup = self._find_duplicate(cells)
            if dup:
                return f"Number {dup} already exists in Column {col}."
        return None

    def _check_subgrids(self, grid) -> str | None:
        for zone_row in range(3):
            for zone_col in range(3):
                cells = grid.get_zone_cells(zone_row, zone_col)
                dup = self._find_duplicate(cells)
                if dup:
                    return f"Number {dup} already exists in the same 3×3 subgrid."
        return None
