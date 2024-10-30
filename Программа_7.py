import random
numba = random.randint (1, 100)
guess = 0
attempts = 0
print('Добро пожаловать в игру Угадай Число!')
print('Загадано число от 1 до 100, твоя задача - угадать число. Поехали!')
while guess != numba:
    guess = int(input('Введите предполагаемое число:'))
    attempts +=1
    if guess<numba:
        print("Загаданное число больше, попробуйте ещё раз.")
    elif guess>numba:
        print("Загаданное число меньше, попробуйте ещё раз.")
    else:
        print("Поздравляю! вы угадали число",numba,"за",attempts,"попыток!")
        print("Спасибо за Игру!")