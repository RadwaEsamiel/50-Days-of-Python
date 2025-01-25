import time
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.penup()
            self.color("black")
            self.score = 0
            self.hideturtle()

        def score_update(self):
            self.clear()
            self.goto(-100, 200)
            self.write(f" Level : {self.score}",
                       font=FONT,
                       align="center"
                       )

        def game_over(self):
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER !!",
                       font=FONT,
                       align="center"
                       )

        def level_up(self):
            self.score += 1
            self.clear()
            self.score_update()
