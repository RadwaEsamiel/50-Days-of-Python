from turtle import Turtle, Screen

tm = Turtle()
tm.shape("arrow")
tm.color("dark blue","light slate blue")
tm.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)

for i in range(20):
    tm.pencolor("dark blue")
    tm.forward(5)
    tm.pencolor("white")
    tm.forward(5)


scr = Screen()
scr.exitonclick()