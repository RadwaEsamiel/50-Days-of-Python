from turtle import Turtle


class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(arg= f"score : {self.Score}",
                   align="center",
            font=("Arial",12,"bold"))
        self.hideturtle()

    def update_board(self):
        self.write(arg=f"score : {self.Score}",
                   align="center",
                   font=("Arial", 12, "bold"))
    def GAME_OVER(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",
                   align="center",
                   font=("Arial", 20, "bold"))

    def win(self):
        self.Score += 1
        self.clear()
        self.update_board()


