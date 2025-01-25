import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)

is_race_on =False

user_bet = screen.textinput(title = "Make your bet!",
                            prompt="Which tutle would you bet on? : ")

colors = ["blue", "orange", "green", "purple", "red","yellow"]

y_pos = [-70,-40,-10,20,50,80]

all_turtles = []


for i in range(0,6) :
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on = True
while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print("you have won!")
                print(f"the winning color is : {winning_color}")
            else:
                print("sorry you have lost")
                print(f"the winning color is : {winning_color}")



        random_dist = random.randint(0,10)
        turtle.forward(random_dist)





screen.exitonclick()