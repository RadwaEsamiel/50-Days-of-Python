word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.


import random
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please guess a letter from the chosen word.").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

letters_of_chosen_word = list(chosen_word)

if guess in letters_of_chosen_word :
    print("Right")
else :
    print("Wrong")
    
___________________________________________________________________________


for letters_of_chosen_word in chosen_word :
    if guess in letters_of_chosen_word :
        print("Right")
    else :
        print("Wrong")