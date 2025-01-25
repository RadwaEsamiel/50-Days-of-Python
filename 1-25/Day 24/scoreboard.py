from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("High_score_data.txt") as file:
    content = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(content)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ** High Score : {self.high_score} **", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("High_score_data.txt", mode= "w") as newfile:
                new_high_score = str(self.high_score)
                newfile.write(new_high_score)

        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
