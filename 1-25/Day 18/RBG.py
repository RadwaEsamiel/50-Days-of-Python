import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
colors = turtle.colormode(255)

def random_mode() :
    red = random.randint(0,255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    random_color =  (red,blue,green)
    return random_color


move = [0,90,180,270]

for x in range(200) :

    for i in range(3,10) :
        color = random_mode()
        tim.pencolor(color)
        tim.forward(30)
        tim.setheading(random.choice(move))
        tim.pensize(i)
        tim.speed("fastest")















screen = Screen()
screen.exitonclick()