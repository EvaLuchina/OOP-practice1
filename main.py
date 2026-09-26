"""Точка входа в игру."""
import sys
from src.game import Game

sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    Game(max_attempts=10).play()


if __name__ == "__main__":
    main()
