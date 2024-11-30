import random
prog = int(input("1 - да, 0 - нет"))
while prog == 1:
    numba = random.randint (1, 100)
    guess = 0
    attempts = 0
    attempts_e = 5
    print('Добро пожаловать в игру Угадай Число!')
    print('Загадано число от 1 до 100, твоя задача - угадать число. Поехали!')
    while guess != numba:
        guess = int(input('Введите предполагаемое число:'))
        attempts +=1
        if guess<numba:
            print("Загаданное число больше, попробуйте ещё раз.")
        elif guess>numba:
            print("Загаданное число меньше, попробуйте ещё раз.")
        elif attempts_e == attempts:
            print("Количество попыток истекло! Правильный ответ:", numba)
            prog=int(input("Продолжить?"))
            if prog == 1:
                attempts = attempts-5  
            else:
                print("Спасибо за игру!")
        else:
            print("Поздравляю! вы угадали число",numba,"за",attempts,"попыток!")
            print("Спасибо за Игру!")
            prog=int(input("Продолжить?"))
            if prog == 1:
                attempts = attempts-5