from turtle import Turtle, Screen

font =  ("Arial", 12, "normal")
align_center = (0,270)

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(align_center)
        self.write(arg=f"score : {self.score}",
                   align="center",
                   font=("Arial", 12, "bold"))
        self.hideturtle()



    def update_board(self):
        self.write(arg=f"score : {self.score}",
                   align="center",
                   font=("Arial", 12, "bold"))
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",
                   align="center",
                   font=("Arial", 20, "bold"))

    def win(self):
        self.score += 1
        self.clear()
        self.update_board()



