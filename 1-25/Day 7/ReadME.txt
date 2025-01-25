Day 7: Hangman Game

In this project, you've built the classic Hangman game. The player must guess the hidden word letter by letter, with a limited number of wrong guesses before the game ends in a loss.

Key Components:
1.External Modules:
utilized hangman_words.py for a list of possible words (word_list).
also imported artwork from hangman_art.py, including the stages of the hangman drawing and the game logo.

2.Random Word Selection:
The game begins by selecting a random word from word_list using random.choice().

3.Displaying the Game Progress:
A list (placeholder) is used to track the letters guessed by the player. Underscores (_) represent unguessed letters, and correct guesses replace the underscores.

4.Lives and Stages:
The player starts with 6 lives. Every incorrect guess decreases the lives, and a different hangman stage is displayed (using the stages list).

5.Game Logic:
The game loops until the player either guesses the word correctly or runs out of lives.

6.Each guess is validated:
If correct, the guessed letter appears in the placeholder.
If incorrect, the player loses a life, and a new stage of the hangman is displayed.
The game ends when all letters are guessed or lives reach zero.