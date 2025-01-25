Day 25 :  U.S. States Game : 
This project is a Python-based interactive game where users attempt to name all 50 U.S. states. The game uses a graphical interface powered by the Turtle module, along with data handling through pandas. The objective is for the user to correctly guess all the states by entering their names. The program provides visual feedback by displaying the name of each correctly guessed state on a U.S. map. If the user types "exit," the game ends, and a file is generated that lists the states that were not guessed.

Key Features

Graphical Interface:
The game displays a blank U.S. map using the Turtle module, creating an engaging and interactive environment for users.
Each correct guess is marked and writted on the map by writing the state’s name at its corresponding location.

User Input and Tracking:
The game continuously prompts users to input state names. Correct guesses are tracked, and users can see their progress in real time.
To end the game prematurely, the user can type "exit." At this point, the game saves the remaining unguessed states to a CSV file for future reference.

State Positioning:
Each state's coordinates (x, y) are preloaded from a CSV file containing state names and their respective coordinates on the map. When a state is guessed correctly, its name is drawn at the appropriate location.

State Validation:
The program ensures that state names are not duplicated by keeping track of previously guessed states.
It also handles invalid or incorrect guesses by informing the user without affecting the flow of the game.

Remaining States CSV:
If the player chooses to exit the game, the program generates a CSV file listing all the states that were not guessed, allowing the user to review the missed states.

Pandas for Data Manipulation: I utilized pandas to manage state data, perform checks, and handle data export, reinforcing my data manipulation skills in Python.

File Handling and Input: learned how to read data from a CSV file, work with structured data, and save outputs (in this case, the remaining unguessed states) back to a file.

Conclusion
This project was a great opportunity to combine graphical programming with data handling in Python. It not only provided an engaging game for users but also highlighted how interactive elements can be implemented using Turtle and pandas. The game presents a fun way to test and enhance users' knowledge of U.S. geography while providing clear feedback and tracking progress.