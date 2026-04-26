class Cell:

    def __init__(self, value=None, is_prefilled=False):
        self._value = value
        self._is_prefilled = is_prefilled
        

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        if self._is_prefilled:
            raise ValueError("Cannot modify a pre-filled cell")
        if value < 1 or value > 9:
            raise ValueError("Value must be between 1 and 9")
        self._value = value

    def clear(self):

        if self.is_prefilled():
            raise ValueError("Cannot modify a pre-filled cell")

        self._value=None

    def is_empty(self):
        return self._value is None

    def is_prefilled(self):
        return self._is_prefilled