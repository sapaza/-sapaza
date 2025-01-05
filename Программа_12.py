m = input("Введите сообщение для шифрования: ")
shift = int(input("Введите сдвиг (число): "))
print ("Вы хотите зашифровать (1) или расшифровать (2) сообщение?")
i = int (input())
if i == 1:
    encrypt = ""
    for char in m:
        if char.isalpha():
            if char.isupper():
                b = ord('A')
            else:
                b = ord('a')
        encrypt += chr ((ord(char) - b + shift) + b)
    print ("Зашифрованное сообщение:", encrypt)
if i == 2: 
    encrypt = ""
    for char in m:
        if char.isalpha():
            if char.isupper():
                b = ord('A')
            else:
                b = ord('a')
        encrypt += chr ((ord(char) -shift))
    print ("Расшифрованное сообщение:", encrypt)