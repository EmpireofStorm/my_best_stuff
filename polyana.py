# CS project
#I wasted so much time on it but I am kinda proud of it
#Names of functions are Russians
from turtle import *

setup(1395, 900)  # Size of window
speed(1000000000)
bgcolor('cyan')  # Background color
title('ПОЛЯНА')  # Name of window
color('light green', 'light green')

def rectangle(x, y):  # Function for making rectangles with x and y sizes
    for i in range(0, 2):
        forward(x)
        rt(90)
        forward(y)
        rt(90)
    rt(270)


def cvetok(x, y, z):  # Function for making one flower, x-stroke color, y-inner color, z-size of petals
    color(x, y)
    begin_fill()
    for i in range(0, 5):
        lepestok(z)
        i = i + 1
    end_fill()


def lepestok(q):  # Function for making one petal with q size
    circle(q, 95)
    lt(85)
    circle(q, 95)
    lt(15)


def cvetochek(x, y, z, a, b):
    width(1)
    begin_fill()
    rectangle(x, y)  # Mostly we will do with 50 20
    end_fill()
    lt(180)
    forward(10)
    rt(90)
    penup()
    forward(10)
    pendown()
    cvetok(z, a, b)  # b mostly would be equal to 20


def pole(x, y, z):
    for i in range(1, x):
        penup()
        color('green', 'green')
        if i >= 10:
            goto(z + i * 50, y)
            pendown()
            if i % 2 == 0:
                lt(170)
                cvetochek(50, 20, 'blue', 'blue', 20)
            else:
                lt(170)
                cvetochek(50, 20, 'red', 'red', 20)

        else:
            goto(z + i * 50, y)
            pendown()
            if i % 2 == 0:
                lt(170)
                cvetochek(50, 20, 'blue', 'blue', 20)
            else:
                lt(170)
                cvetochek(50, 20, 'red', 'red', 20)


width(5)
penup()
# Making grass
goto(695, -430, -550)
pendown()
lt(180)
begin_fill()
rectangle(695 * 2, 450)
penup()
end_fill()
# Grass is over
# Flower №1
goto(-600, -300)
color('green', 'green')
pendown()
cvetochek(50, 20, 'red', 'red', 20)
# Flower 1 over
# Flower 2 start
penup()
goto(-550, -300)
pendown()
color('green', 'green')
lt(170)
cvetochek(50, 20, 'blue', 'blue', 20)
pole(23, -300, -550)
pole(25, -370, -650)
