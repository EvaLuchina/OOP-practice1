# Исходный код

```
# Исходный процедурный код (только для чтения и анализа)

import random

def play_guess_number_procedural():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Я загадал число от 1 до 100. У вас 10 попыток.")
    while attempts < max_attempts:
        try:
            guess = int(input("Ваш вариант: "))
        except ValueError:
            print("Введите число!")
            continue
        attempts += 1
        if guess < secret:
            print("Больше!")
        elif guess > secret:
            print("Меньше!")
        else:
            print(f"Угадали! Попыток: {attempts}")
            return
    print(f"Попытки закончились. Было загадано: {secret}")

print("Функция определена, готова к анализу")
```

# 1.1 Таблица анализа

| Что | Где в исходном коде | Куда перенести |
| --- | --- | --- |
| Генерация числа | secret = random.randint | Game() |
| Текущая попытка | attempt = ... | Player() |
| Количество попыток | max_attempts = ... | Game() |
| Попытка игрока | input("Ваш вариант: ") | Player() |
| Проверка ввода | try:...except ValueError: | Player() |
| Сравнение чисел | if guess < secret: ... | Game() |
| Лимит попыток | while attempts < max_attempts: ... | Game() |
| Вывод сообщений | print(...) | UI() |
| Ввод | input(...) | UI() |



# 1.2

## 1. Какие классы вы выделите? Обоснуйте.

1. Game() - выбор числа и игровой цикл
2. Player() - ввод с валидацией и подсчет попыток
3. UI() - все вводы и выводы

## 2. Какие атрибуты будут приватными? Почему?

### Game() 

1. self.__secret_number - нельзя менять загаданное число
2. self.__max_attempts - нельзя менять количество попыток

### Player()

1. self.__attempts - нельзя менять текущую попытку

## 3. Какие методы будут публичными? Почему?

### UI() 

1. show_message()
2. get_input()

Все методы публичные так как используются для ввода и вывода

### Game()

1. play() - для вызова начала игры

### Player() 

1. make_guess() - используется в Game() при сравнении с загаданным числом
2. count_attempts() - используется в Game() при проверке оставшихся попыток

## 4. Есть ли в исходном коде «God Object»? Как вы это поняли?

Да, есть. Это функция play_guess_number_procedural(). В ней описана вся логика, процесс игры, ввод, вывод и ошибки