import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print("The number of letters: " + placeholder)


# TODO-1: Use a while loop to let the user guess again
# TODO-2: Update the for loop so that previous guesses are added to the display String.

display_list = []

while True :

    guess = input("Please guess a letter from the chosen word.\n").lower()
    if guess in chosen_word :
        print("Right guess")
    else :
         print("Wrong guess")

    for letter in chosen_word :
        if guess == letter :
            display_list.append(guess)
    print(display_list)

    display_word = ""
    for letters in chosen_word :
        if letters in display_list :
            display_word += letters
        else :
            display_word += "_"


    print(display_word)

    if "_" not in display_word :
        print("You Win! congratulation!")
        break





