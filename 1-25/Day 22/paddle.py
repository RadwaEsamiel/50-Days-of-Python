from turtle import Turtle, Screen


class Paddle(Turtle) :
    def __init__(self,position_x):
        super().__init__()
        self.penup()
        self.speed("fast")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position_x, 0)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.sety(new_y)
