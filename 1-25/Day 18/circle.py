import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
colors = turtle.colormode(255)
tim.speed("fastest")

def random_color_palet() :
    red = random.randint(0,255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    random_color =  (red,blue,green)
    return random_color

def draw_circle() :
    color = random_color_palet()
    tim.pencolor(color)
    tim.circle(100)
    tim.penup()
    tim.setheading(tim.heading() + 5)
    tim.pendown()

for i in range(200) :
    draw_circle()



screen = Screen()
screen.exitonclick()