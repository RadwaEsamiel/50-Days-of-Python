Day 14: The Higher Lower GAME :
the project involved creating a "Higher Lower" game where players compare follower counts of two random celebrities, with the objective of guessing which one has more followers.

The project required multiple elements:

Game Structure:
The game introduces two random celebrities selected from a dataset containing their names, descriptions, countries, and follower counts in a dictionary format.
Players are prompted to choose between two options, "A" or "B," based on their guess of who has the higher follower count.

Data and Comparison:
The celebrity data is stored in a separate module (game_data), containing details like their name, profession, country, and follower count.
Random selections are made from this dataset for comparison. The player's task is to correctly guess which celebrity has more followers.

Game Continuity:
If the player guesses correctly, the score increases, and the game continues with a new comparison using the celebrity (A) against a new random celebrity (B).
If the player guesses incorrectly, the game ends, and the final score is displayed.

User Input and Validation:
The program handles invalid inputs (anything other than 'A' or 'B') by prompting the player to choose again.
A user-friendly loop structure is used to allow continuous gameplay until the player chooses to exit or makes a wrong guess.

Visual Design:
The game uses ASCII art from the art module to enhance the visual appeal. Logos and a visual separator (VS) are displayed to distinguish between the two celebrity comparisons.
This project emphasizes core programming concepts such as loops, conditionals, random selections, and user input handling, while also making the game interactive and fun for the player.