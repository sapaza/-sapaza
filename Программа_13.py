import random

t = ("бриллианты", "рубины", "изумруды", "золотые монеты", "жемчуг")

chest1 = ()
chest2 = ()
chest3 = ()

for i in range(5):
    chest1 = chest1 + (random.choice(t),)
    chest2 = chest2 + (random.choice(t),)
    chest3 = chest3 + (random.choice(t),)

print("Сундук 1:", chest1)
print("Сундук 2:", chest2)
print("Сундук 3:", chest3)