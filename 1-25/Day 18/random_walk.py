from turtle import Turtle, Screen
import random

colors = ["saddle brown","light slate gray", "dark blue","cyan", "spring green", "gold", "dark khaki", "brown", "crimson", "deep pink",  "orchid", "medium purple" ]
tim = Turtle()
move = [0,90,180,270]
speed =["fastest","fast","normal","slow","slowest"]

for x in range(200) :
    for i in range(3,10) :
        tim.pencolor(random.choice(colors))
        tim.forward(30)
        tim.setheading(random.choice(move))
        tim.pensize(i)
        tim.speed(random.choice(speed))















screen = Screen()
screen.exitonclick()