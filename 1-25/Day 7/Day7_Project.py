
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
word_list = hangman_words.word_list

# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
import hangman_art
stages = hangman_art.stages

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

import random
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print("The number of letters: " + placeholder)

display_list = []

while True :

    guess = input("Please guess a letter from the chosen word.\n").lower()

    if guess in chosen_word :
        print("Right guess")
        if guess in display_list :
            print(f"You've already guessed {guess}")
    else :
        lives -= 1
        print(f"You guessed {guess}, that's not in the word."
              f" You lose a life.\n****************************You have {lives} Lives Left****************************")
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
        print(f"***********************You Win!***********************"
              f"\nThe word is {display_word} congratulation!")
        break
    elif lives == 0 :
        print(f"***********************You Lose!***********************"
              f"\nThe word was {chosen_word}")
        break


