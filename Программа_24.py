import turtle
import random
def random_color():
    return (random.random(),random.random(),random.random())
z = random.randint(3,12)
turtle.penup()
turtle.backward(400)
turtle.pendown()
for _ in range (z):
    turtle.color(random_color())
    a = random.randint(3,12)
    turtle.begin_fill()
    for _ in range (a):
        turtle.forward(25)
        turtle.left(360/a)
    turtle.end_fill()
    turtle.penup()
    turtle.forward (75)
    turtle.pendown()
turtle.done()