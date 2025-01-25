from turtle import Turtle, Screen


class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()


    def score_update(self):
        self.clear()
        self.goto(-100,200)
        self.write(f" Score : {self.right_score}",
                   font=("Arial",20,"normal"),
                   align= "center"
                   )
        self.goto(100,200)
        self.write(f" Score : {self.left_score}",
                   font=("Arial",20,"normal"),
                   align= "center"
                   )

    def r_point(self):
        self.right_score += 1
        self.score_update()

    def l_point(self):
        self.left_score += 1
        self.score_update()

