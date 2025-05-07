import turtle

def draw_koch(order,size):
    if order == 0:
        turtle.forward(size)
    else:
        draw_koch(order - 1, size/3)
        turtle.left(60)
        draw_koch(order - 1, size/3)
        turtle.right(120)
        draw_koch(order - 1, size/3)
        turtle.left(60)
        draw_koch(order - 1, size/3)

def draw_snowflake():
    for _ in range(3):
        draw_koch(4,400)
        turtle.right(120)

def main_koch():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,200)
    turtle.pendown()
    draw_snowflake()
    turtle.done()
main_koch()