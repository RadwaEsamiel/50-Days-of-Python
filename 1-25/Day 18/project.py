import turtle
import random
from turtle import Screen

turtle.colormode(255)




tim = turtle.Turtle()
color_pal = [
    (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48),
    (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36),
    (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147),
    (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167)
]

tim.speed("fastest")
tim.penup()
tim.hideturtle()


tim.goto(-300, 300)

number_of_dots = 1000
dots_per_row = 20
dot_size = 20
spacing = 30

for i in range(number_of_dots):
    tim.dot(dot_size, random.choice(color_pal))
    tim.forward(spacing)

    if (i + 1) % dots_per_row == 0:
        tim.setheading(270)
        tim.forward(spacing)
        tim.setheading(180)
        tim.forward(spacing * dots_per_row)
        tim.setheading(0)

screen = Screen()

screen.exitonclick()
