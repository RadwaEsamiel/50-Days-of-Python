import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Please guess a letter from the chosen word.").lower()


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
placeholder = ""

for letter in chosen_word :
    if guess == letter :
        placeholder += guess
    else :
        placeholder += "_"


if guess in chosen_word :
    print("Right")
else :
     print("Wrong")

print(placeholder)