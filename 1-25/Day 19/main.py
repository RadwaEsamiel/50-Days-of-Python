from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)

def move_backwards():
    tim.backward(100)

def turn_left():
    tim.left(50)
def turn_right():
    tim.right(50)

def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()



screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="l",fun=turn_left)
screen.onkey(key="r",fun=turn_right)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()