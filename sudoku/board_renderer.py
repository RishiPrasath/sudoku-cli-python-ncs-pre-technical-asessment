class BoardRenderer:

    ROW_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    def render(self, grid) -> str:
        lines = []

        # Column header
        lines.append("    1 2 3 4 5 6 7 8 9")

        for label in self.ROW_LABELS:
            row_cells = grid.get_row_cells(label)
            values = []
            for cell in row_cells:
                values.append(str(cell.get_value()) if not cell.is_empty() else "_")
            row_str = f"  {label} {' '.join(values)}"
            lines.append(row_str)

        output = "\n".join(lines)
        print(output)
        return output
