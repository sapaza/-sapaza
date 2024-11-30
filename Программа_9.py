import re
text = "  Привет, Капитан Блэк! Я нашел сокровище!  "
textX = text.strip( )
a = textX[0:7]
b = textX[8:21]
c = textX[22:40]
x = a.lower()
y = b.upper()
z = c.replace("сокровище","карту")
result = x + " " + y + " " + z
print(result)