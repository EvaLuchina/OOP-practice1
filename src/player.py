"""Игрок."""

from .ui import UI


class Player:
    """Игрок: имя, счётчик попыток, взаимодействие с UI."""

    def __init__(self, ui: UI):
        self._attempts = 0
        self._ui = ui

    @property
    def attempts(self) -> int:
        return self._attempts

    def make_guess(self) -> int:
        """Запросить у игрока целое число.

        Повторяет запрос при неверном вводе.
        """
        while True:
            try:
                return int(self._ui.get_input("Вы считаете загаданое число это: "))
            except ValueError:
                self._ui.show_message("Вы ввели не целое число...")

    def count_attempts(self) -> None:
        """Увеличить счётчик попыток на 1."""
        self._attempts += 1
