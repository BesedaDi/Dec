import turtle
from turtle import *
# Ввод данных
# с использованием диалоговых окон
xc = numinput("Координаты центра окружности", "Введите xc", 0, minval=-300, maxval=300)
yc = numinput("Координаты центра окружности", "Введите yc", 0, minval=-300, maxval=300)
r = numinput("Окружность", "Введите радиус r ", 0, minval=0, maxval=300)
x = numinput("Координаты точки", "Введите x", 0, minval=-300, maxval=300)
y = numinput("Координаты точки", "Введите y", 0, minval=-300, maxval=300)

reset() #  Приводим черепашку в начальное положение
hideturtle() # Скрыть указатель черепашки
penup()
def polygon(t, length, n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360 / n)
def circle(t, r):
    circumference = 2 * 3.14 * r
    length = circumference / 360
    polygon(t, length, 360)
def main ():
    circle(bob, 200)
    turtle.done()
# Допишите здесь решение задачи
# Других файлов создавать не нужно


done()