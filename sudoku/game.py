class Game:

    def __init__(self, attempt_grid, solution_grid, renderer, validator, hint_engine, parser):
        self._attempt = attempt_grid
        self._solution = solution_grid
        self._renderer = renderer
        self._validator = validator
        self._hint_engine = hint_engine
        self._parser = parser

    def run(self):
        print("\nWelcome to Sudoku!\n")
        print("Here is your puzzle:")
        self._renderer.render(self._attempt)

        while True:
            raw = input("\nEnter command (e.g., A3 4, C5 clear, hint, check, quit): ").strip()
            command = self._parser.parse(raw)

            if command is None:
                print("Invalid command. Try: A3 4 | C5 clear | hint | check | quit")
                continue

            cmd_type = command["type"]

            if cmd_type == "place":
                msg = self._place(command["row"], command["col"], command["value"])
                print(f"\n{msg}")
                if "accepted" in msg:
                    print("\nCurrent grid:")
                    self._renderer.render(self._attempt)
                    if self._check_win():
                        print("\nYou have successfully completed the Sudoku puzzle!")
                        if self._play_again():
                            return self.run()
                        return
                else:
                    print("\nCurrent grid:")
                    self._renderer.render(self._attempt)

            elif cmd_type == "clear":
                msg = self._clear(command["row"], command["col"])
                print(f"\n{msg}")
                print("\nCurrent grid:")
                self._renderer.render(self._attempt)

            elif cmd_type == "check":
                print(f"\n{self._check()}")

            elif cmd_type == "hint":
                print(f"\n{self._hint()}")

            elif cmd_type == "quit":
                self._quit()
                return

    def _place(self, row, col, value) -> str:
        cell = self._attempt.get_cell(row, col)
        if cell.is_prefilled():
            return f"Invalid move. {row}{col} is pre-filled."
        try:
            self._attempt.set_cell(row, col, value)
            return "Move accepted."
        except ValueError as e:
            return f"Invalid move. {e}"

    def _clear(self, row, col) -> str:
        cell = self._attempt.get_cell(row, col)
        if cell.is_prefilled():
            return f"Invalid move. {row}{col} is pre-filled."
        self._attempt.clear_cell(row, col)
        return f"Cell {row}{col} cleared."

    def _check(self) -> str:
        result = self._validator.check(self._attempt)
        if result:
            return result
        return "No rule violations detected."

    def _hint(self) -> str:
        return self._hint_engine.get_hint()

    def _quit(self):
        print("Thanks for playing. Goodbye!")

    def _check_win(self) -> bool:
        if not self._attempt.is_complete():
            return False
        return self._validator.check(self._attempt) is None

    def _play_again(self) -> bool:
        answer = input("\nPress any key to play again (or 'n' to quit): ").strip().lower()
        return answer != "n"
