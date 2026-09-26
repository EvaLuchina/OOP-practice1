# UML диаграмма классов

```mermaid
classDiagram
    class Game {
        -secret_number: int
        -max_attempts: int
        -ui: UI
        +play(): void
        +check_guess(guess: int): str
        +secret_number: int
    }
    class Player {
        -attempts: int
        -ui: UI
        +make_guess(): int
        +count_attemptss(): void
        +attempts: int
    }
    class UI {
        +show_message(message: str): void
        +get_input(prompt: str): str
    }
    Game --> UI : uses
    Game --> Player : creates
    Player --> UI : uses
```


## 1. Есть ли у вас наследование
Нет

## 2. Есть ли композиция? Что чем владеет?
Композиция есть. Game создаёт Player
Game владеет secret_number, max_attempts, ui
Player владеет attempts, ui
UI не владеет ничем

## 3. Есть ли циклические зависимости?
Нет