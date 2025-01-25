Day 11: Blackjack Game Documentation
This is a command-line implementation of the classic card game Blackjack, allowing a user to play against the computer. The game follows typical Blackjack rules where the player and the computer (dealer) are dealt two cards, and the goal is to get as close to 21 points without exceeding it. The player can request additional cards or stand, and the dealer follows basic rules to either draw or stop based on their score.

Modules and Files
1.art.py
Contains art/logo for the game.
Displays the game logo at the start of the game when the player decides to play.

2.cards
Contains a list of cards available in the game.
Card values include Aces ('A'), number cards (2 to 10), and face cards ('J', 'Q', 'K').
Aces can have values of either 1 or 11, while face cards are valued at 10.

3.function
Contains the game() function, which manages the core game logic, including:
Determining if the player or computer has a Blackjack.
Handling Ace card values (1 or 11 based on score).
Calculating player and computer scores.
Checking for win conditions and ending the game when applicable.

4.winner_function
Contains the winner() function that determines the winner after both the player and computer finish drawing cards.
Compares the player's and the computer's final scores and prints the result.

Main Game Loop

Initialization
The game begins by asking the player whether they want to play a game of Blackjack ('y' or 'n').
If the player selects 'y', two cards are dealt to both the player and the computer.

Player's Turn
The player’s initial two cards are displayed along with the computer’s first card (the second card remains hidden).
The player is asked if they want to draw another card by typing 'y' or pass by typing 'n'.
If the player draws another card and their score exceeds 21, the player loses.
If the player stands, the computer's turn begins.


Computer's Turn
The computer draws cards until its score reaches at least 16 points.
If the computer's score exceeds 21, the player automatically wins.

End of Game
The final scores for both the player and the computer are displayed.
The game checks for Blackjack conditions (where either the player or the computer has a Blackjack "both Ace and face card" from the start the computer wins if it has both even if player has Blackjack as well).
The winner() function is called to decide the outcome based on both players' scores.

Key Functions

1.game(computer_cards, user_cards)

This function processes the gameplay. 
it Checks if any of the initial hands (player or computer) contains a Blackjack (21).
Calculates and adjusts the value of the Ace based on whether it should count as 1 or 11.
Calculates and adjusts the value of the face cards to count as 10.
Returns the user's score, computer's score, and a flag indicating if the game is over.

2.winner(user_cards, computer_cards)

This function determines the winner at the end of the game:
If the player’s score exceeds 21, they lose.
If the computer’s score exceeds 21, the player wins.
Otherwise, the scores are compared to decide the winner.
The player can choose to start a new game or exit.

3.Card Value Logic

Ace ('A'): Can be either 1 or 11. The value is automatically adjusted based on the total score (11 if the score doesn’t exceed 21, else 1).
Face Cards ('J', 'Q', 'K'): These are valued at 10.
Number Cards (2 to 10): Retain their numeric value.