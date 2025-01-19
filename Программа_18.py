attempts = 6
word = ["г", "р", "у", "ш", "а"]
word1 = {
    'г':1,
    'р':2,
    'у':3,
    'ш':4,
    'а':5
             }
print("Добро пожаловать в игру 'Угадай число!'")
o = "".join(word)
test = ['_','_','_','_','_']
while attempts != 0:
    letter = input("Угадай Букву: ")
    n = word1.get(letter)
    if letter in word:
        print (letter, "в слове!")
        test[n-1]=letter
        print(''.join(test))
    elif letter not in word:
        attempts -= 1
        print("Буквы в слове нет! Осталось", attempts, "попыток!")
        if attempts == 0:
            print("Игра окончена! Слово:",o)
