from random import choice
from turtle import Turtle, Screen
import random

tm = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'pink', 'brown', 'cyan', 'magenta']
tm.shape("arrow")
tm.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)

for triangle in range(3):
    tm.pencolor(random.choice(colors))
    tm.forward(100)
    tm.left(120)

for square in range(4) :
    tm.pencolor(random.choice(colors))
    tm.forward(100)
    tm.left(90)

for pentagon in range(5) :
    tm.pencolor(random.choice(colors))
    tm.forward(100)
    tm.left(72)






scr = Screen()
scr.exitonclick()