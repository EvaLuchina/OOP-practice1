"""Тесты класса Game."""

from src.game import Game


class TestGame:
    """Проверяем логику проверки попытки."""

    def test_check_guess_too_low(self):
        """Если попытка меньше секрета — «Недобор»."""
        g = Game()
        g._secret_number = 50
        assert g.check_guess(30) == "Недобор"

    def test_check_guess_too_high(self):
        """Если попытка больше секрета — «Перебор»."""
        g = Game()
        g._secret_number = 50
        assert g.check_guess(70) == "Перебор"

    def test_check_guess_correct(self):
        """Если попытка равна секрету — «Ура ура победа!»."""
        g = Game()
        g._secret_number = 50
        assert g.check_guess(50) == "Ура ура победа!"

    def test_secret_property(self):
        """Свойство secret возвращает целое число."""
        g = Game()
        assert isinstance(g.secret, int)
