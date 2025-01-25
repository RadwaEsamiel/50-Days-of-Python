from random import choice
from turtle import Turtle, Screen




tm = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'pink', 'brown', 'cyan', 'magenta']
tm.shape("arrow")
tm.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)

def shape_drawing(sides) :
    shape = 360 / sides
    for i in range(sides) :
        tm.pencolor(choice(colors))
        tm.forward(100)
        tm.left(shape)


for x in range(3,10) :
    shape_drawing(x)

screen =Screen()
screen.exitonclick()