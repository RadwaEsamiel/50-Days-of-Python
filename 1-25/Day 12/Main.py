import Intro
import random
import Function
print(Intro.intro_logo)
print(Intro.intro_statement)


new_game = True

while new_game :
    start = input("Type 'y' to Start A new Game, type 'n' to Exit:").lower()
    if start == 'y' :
        def_level = input("I'm thinking of a number between 1 and 100\n"
                          "Now Choose difficulty Level.\n"
              "Type 'easy' to get 10 Attempts or 'hard' to get only 5 Attempts: ").lower()

        if def_level == 'easy':
            Function.guess_game(10)
        elif def_level == 'hard':
            Function.guess_game(5)

    elif start == 'n' :
        new_game = False
    else:
        print("Invalid Answer!")
        continue








