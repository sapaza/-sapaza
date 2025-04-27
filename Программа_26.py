import turtle, random
turtle.Screen().bgcolor("skyblue")
def draw_grass():
    turtle.penup()
    turtle.goto(-400,-200)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()

def draw_house():
    turtle.penup()
    turtle.goto(-100,-200)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()
    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(-100,0)
    turtle.goto(0,100)
    turtle.goto(100,0)
    turtle.end_fill()

def draw_cloud(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.circle(random.randint(10,30))
        turtle.right(random.randint(30,90))
    turtle.end_fill()

def draw_sun():
    turtle.penup()
    turtle.goto(-300,200)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_tree(x,y,h):
    turtle.penup()
    turtle.goto (x,y)
    turtle.pendown()
    turtle.color("brown")
    turtle.right(180)
    turtle.begin_fill()
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.right(90)
    turtle.goto(x-30,y+h)
    for _ in range(3):
        turtle.color('green')
        turtle.begin_fill()
        turtle.circle(random.randint(20,36))
        turtle.forward(50)
        turtle.end_fill()

        
draw_grass()
draw_house()
draw_tree(-185,-200, 150)
draw_tree(215,-200, 150)
draw_sun()
draw_cloud(-150,150)
draw_cloud(-50, 180)
draw_cloud(-250,130)

turtle.done()