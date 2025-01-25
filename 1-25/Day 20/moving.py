import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initial positions for the squares
positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.shapesize(stretch_wid=1, stretch_len=1)
    new_turtle.goto(pos)
    segments.append(new_turtle)



game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) -1, 0 ,-1) :
        new_x = segments[seg -1 ].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)


screen.exitonclick()
