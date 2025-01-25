Day 12 Project: Number Guessing Game Documentation

The goal was to create a number guessing game similar to the provided demo. The game should allow the user to guess a randomly chosen number between 1 and 100, while limiting the number of attempts based on the difficulty level selected by the player. There were no specific hints or detailed instructions provided, so the task was to replicate the demo using creativity and problem-solving.

Key Features:
Random Number Generation: A random number is generated between 1 and 100 at the start of the game.
Difficulty Levels: The user can select between 'easy' (10 attempts) and 'hard' (5 attempts).
User Interaction: The user makes guesses, and the game responds with feedback ("Too High", "Too Low") until the correct number is guessed or the attempts run out.
Input Validation: Input is validated to ensure it is a valid number within the specified range.

Files in the Project:
Intro.py: This module contains the ASCII art for the game logo and an introductory statement.
Function.py: This module contains the guess_game function, which implements the core logic of the game.
Main Program: This is where the game starts, providing the user with the option to start a new game, choose the difficulty level, and play the number guessing game.


Step-by-Step Explanation:
1. Generating the Logo (Intro.py)
started by creating a logo using an ASCII art generator from the website patorjk.com, which adds a fun visual element to the game. This logo was stored in the Intro.py module.

2. Core Game Logic (Function.py)
In Function.py, wrote the core of the number guessing game with the guess_game() function. 

This function handles:
Generating a random number between 1 and 100.
Checking if the user's input is a valid guess (numeric and within range).
Giving feedback if the guess is too high or too low.
Handling the number of attempts based on the chosen difficulty level.

Key parts include:
Random Number Generation: Using random.choice(range(1, 101)) to generate a number between 1 and 100.
Input Validation: Checking if the user's input is a valid number using .isnumeric().
Feedback: Providing feedback if the guess is "Too High" or "Too Low" and reducing the number of attempts accordingly.
Game Over Condition: If the player runs out of attempts or guesses the correct number, the game ends.

3. Main Game Logic (Main Program)
In the main part of your program, is the set up the overall flow for the game. This part allows users to start a new game, select a difficulty level, and exit the game.
