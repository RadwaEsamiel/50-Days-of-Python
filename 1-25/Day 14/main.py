import art
import function

print(art.logo)
print("Welcome to OUR higher lower game!")
new_game = True

while new_game :
    start = input("Type 'y' to Start A new Game, type 'n' to Exit:").lower()


    if start == 'y' :
        print("\n" * 100)
        print(art.logo)
        print("Welcome to OUR higher lower game!")
        function.higher_lower_game()
    elif start == 'y' :
        break
    else :
        print("Invalid Answer!")
        continue