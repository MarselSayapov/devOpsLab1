def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    secret_number = 42  # Установим число для угадывания
    attempts = 0

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1
            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите число.")


guess_number()
