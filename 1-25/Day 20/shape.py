from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Initial positions for the squares
positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.fillcolor("white")
    new_turtle.penup()
    new_turtle.shapesize(stretch_wid=1, stretch_len=1)
    new_turtle.goto(pos)

screen.exitonclick()
