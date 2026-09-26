"""Игра «Угадай число»."""

import random
from .ui import UI
from .player import Player


class Game:
    """Управляет игровым циклом «Угадай число».

    Отвечает за:
    - генерацию секретного числа;
    - создание игрока;
    - проверку попыток;
    - завершение игры.
    """

    def __init__(self, max_attempts: int = 10, ui: UI | None = None):
        self._max_attempts = max_attempts
        self._secret_number = 0
        self._ui = ui if ui is not None else UI()

    def play(self) -> None:
        """Запустить игровой цикл."""
        self._secret_number = random.randint(1, 100)
        self._ui.show_message(
            f"Я загадал число от 1 до 100. У вас {self._max_attempts} попыток. Удачи!"
        )
        player = Player(self._ui)
        while player.attempts < self._max_attempts:
            guess = player.make_guess()
            player.count_attempts()
            result = self.check_guess(guess)
            self._ui.show_message(result)
            if guess == self._secret_number:
                return
        self._ui.show_message(
            f"Вы не угадали... (Грустные звуки скрипки) Было загадано: {self._secret_number}"
        )

    def check_guess(self, guess: int) -> str:
        """Вернуть сообщение-подсказку для попытки."""
        if guess < self._secret_number:
            return "Недобор"
        elif guess > self._secret_number:
            return "Перебор"
        return "Ура ура победа!"

    @property
    def secret(self) -> int:
        """Секретное число (только чтение; используется в тестах)."""
        return self._secret_number
