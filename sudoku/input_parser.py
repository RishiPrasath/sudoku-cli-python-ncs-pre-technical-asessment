class InputParser:

    VALID_ROWS = set("ABCDEFGHI")
    SINGLE_COMMANDS = {"hint", "check", "quit"}

    def parse(self, raw_input: str) -> dict | None:
        if not raw_input or not raw_input.strip():
            return None

        tokens = raw_input.strip().upper().split()

        # Single word commands
        if len(tokens) == 1:
            cmd = tokens[0].lower()
            if cmd in self.SINGLE_COMMANDS:
                return {"type": cmd}
            return None

        # Two token commands: "A3 4" or "A3 clear"
        if len(tokens) == 2:
            cell_token = tokens[0]
            action_token = tokens[1]

            # Validate cell token — must be letter + digit(s)
            if len(cell_token) < 2:
                return None

            row = cell_token[0]
            if row not in self.VALID_ROWS:
                return None

            try:
                col = int(cell_token[1:])
            except ValueError:
                return None

            if col < 1 or col > 9:
                return None

            # Clear command
            if action_token == "CLEAR":
                return {"type": "clear", "row": row, "col": col}

            # Place command — action_token must be a digit 1-9
            try:
                value = int(action_token)
            except ValueError:
                return None

            if value < 1 or value > 9:
                return None

            return {"type": "place", "row": row, "col": col, "value": value}

        return None
