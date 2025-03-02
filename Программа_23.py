from turtle import *

length = int(input("Введите длину лучиков в снежинке: "))
num = int(input("Введите количество лучиков: "))


def draw_snow():
    u=0
    ang = 360/num
    while u<=num:
        forward(length)
        backward(length)
        right(ang)
        u+=1
speed(0)        
draw_snow()

done()