from turtle import *
speed(0)

def move_fd():
    setheading(90)
    fd(10)
def rotate_lt():
    setheading(180)
    fd(10)
def move_bd():
    setheading(270)
    fd(10)
def rotate_rt():
    setheading(0)
    fd(10)
def move_stop(x,y):
    goto(x,y)
    home()
def red():
    color("red")
def green():
    color("green")
def blue():
    color("blue")
screen = Screen()

screen.onkeypress(move_fd,"w")
screen.onkeypress(rotate_lt,"a")
screen.onkeypress(move_bd,"s")
screen.onkeypress(rotate_rt,"d")
screen.onkeypress(red,"r")
screen.onkeypress(green,"g")
screen.onkeypress(blue,"b")


screen.onscreenclick(move_stop)

screen.listen()
screen.mainloop()
