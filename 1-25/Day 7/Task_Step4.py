stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print("The number of letters: " + placeholder)

display_list = []

# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
#  If lives goes down to 0 then the game should stop and it should print "You lose."


while True :

    guess = input("Please guess a letter from the chosen word.\n").lower()

    if guess in chosen_word :
        print("Right guess")
    else :
        lives -= 1
        print(f"Wrong guess. {lives} Lives Left.")
        print(stages[lives])


    display_word = ""

    for letter in chosen_word :
        if guess == letter :
            display_word += letter
            display_list.append(guess)
        elif letter in display_list :
            display_word += letter
        else :
            display_word += "_"


    print(display_word)

    if "_" not in display_word :
        print("You Win! congratulation!")
        break
    elif lives == 0 :
        print("You Lose! ")
        break



    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.

