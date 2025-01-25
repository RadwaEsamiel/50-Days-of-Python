print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road_answer= input("You have come into a two ways road. which are you going to take? \nLeft or Right?").lower()
if road_answer == "right" :
    print("you have fallen into a Hole!\n GAME OVER!!")
elif road_answer == "left" :
    lake_answer = input("Now you can see a lake in your way. what are you going to do? \nSwim or Wait? ").lower()
    if lake_answer == "swim" :
        print("You have been attacked by trout!\n GAME OVER!!")
    elif lake_answer == "wait" :
        door_answer = input("You have coma across a road with a few doors to open\nEach Door has a different color Yellow,Red,Blue\n which door are you going to open first? ").lower()
        if door_answer == "red" :
            print("You are burned by fire!\n GAME OVER!!")
        elif door_answer == "blue" :
            print("You are eaten by beasts!\n GAME OVER!!")
        elif door_answer == "yellow" :
            print("You WIN!! Congratulations!")
        else :
            print("GAME OVER!!")

    else :
        "Please Choose a correct answer. Either Swim or Wait."

else :
    print("Please Choose a correct answer. Either Right or Left.")

