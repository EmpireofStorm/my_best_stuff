# Проект по информатике
from turtle import *

setup(1395, 900)  # Размеры окна с результатом рисования
speed(1000000000)
bgcolor('cyan')  # Цвет фона
title('ПОЛЯНА')  # Название окна с результатом рисования
color('light green', 'light green')  # Первая строка-цвет обводки, вторая-цвет заливки


def rectangle(x, y):  # Функция для создания прямоугольников длиной x и шириной y
    for i in range(0, 2):
        forward(x)
        rt(90)
        forward(y)
        rt(90)
    rt(270)


def cvetok(x, y, z):  # Функция для создания одного цветка, где x-цвет обводки, y-цвет заливки, z-длина лепестков
    color(x, y)
    begin_fill()
    for i in range(0, 5):
        lepestok(z)
        i = i + 1
    end_fill()


def lepestok(q):  # Функция для создания одного лепестка, q-радиус дуги
    circle(q, 95)
    lt(85)
    circle(q, 95)
    lt(15)


def cvetochek(x, y, z, a, b):
    width(1)
    begin_fill()
    rectangle(x, y)  # Чаще всего мы будем делать 50 20
    end_fill()
    lt(180)
    forward(10)
    rt(90)
    penup()
    forward(10)
    pendown()
    cvetok(z, a, b)  # b чаще всего будет 20


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
# Делаем траву
goto(695, -430, -550)
pendown()
lt(180)
begin_fill()
rectangle(695 * 2, 450)
penup()
end_fill()
# Трава закончена
# Начало цветка №1
goto(-600, -300)
color('green', 'green')
pendown()
cvetochek(50, 20, 'red', 'red', 20)
# Цветок №1 закончен
# Начало цветка №2
penup()
goto(-550, -300)
pendown()
color('green', 'green')
lt(170)
cvetochek(50, 20, 'blue', 'blue', 20)
pole(23, -300, -550)
pole(25, -370, -650)
