
import turtle
from turtle import Turtle, Screen

import pandas as pd


data = pd.read_csv("50_states.csv")
states_list = []
for state in data.state :
    states_list.append(state.lower())


screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.title("USA States Game!!")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

writer = Turtle()
writer.penup()
writer.color("black")
writer.hideturtle()

remaining_states = states_list.copy()


while len(remaining_states) > 0 :
    remaining_states_number = len(states_list) - len(remaining_states)
    user_answer = screen.textinput(title=f"You have guessed {remaining_states_number}/{len(states_list)} ",
                                   prompt="What's another State's name in the USA? ")

    if user_answer.lower() == "exit":
        df_remaining_states = pd.DataFrame(remaining_states)
        df_remaining_states.to_csv("The Remaining Unguessed States")
        break

    elif user_answer.lower() in remaining_states :
            print("You Are right")
            remaining_states.remove(user_answer.lower())
            state_cor =  data[data.state.str.lower() == user_answer.lower()]
            x_cor = state_cor.x.values[0]
            y_cor = state_cor.y.values[0]
            writer.goto(x_cor, y_cor)
            writer.write(f" {user_answer.lower()}",
                         font=("Arial", 12, "normal"),
                         align="center"
                         )



    elif user_answer.lower() in states_list:
        print("State Already guessed before")


    else:
        print("you are wrong")



turtle.mainloop()