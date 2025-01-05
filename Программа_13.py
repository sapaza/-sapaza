import random

t = ("бриллианты", "рубины", "изумруды", "золотые монеты", "жемчуг")

chest1 = ""
chest2 = ""
chest3 = ""
x = 2

chest1 = random.choice(t)
chest2 = random.choice(t)
chest3 = random.choice(t)

while x<=5:
     chest1 = chest1 + ", " + random.choice(t)
     chest2 = chest2 + ", " + random.choice(t)
     chest3 = chest3 + ", " + random.choice(t)
     x+=1

print("Сундук 1:", chest1)
print("Сундук 2:", chest2)
print("Сундук 3:", chest3)