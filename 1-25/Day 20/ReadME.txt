In Day 20 and 21's project, the focus is on creating a classic Snake Game using the turtle module in Python. This project demonstrates how to manage game loops, handle user input, and work with object-oriented programming principles by breaking down the game into manageable classes: Snake, Food, and Scoreboard.

1. Snake Initialization:
   - The snake is created using the `Snake` class, which initializes the snake with a few segments. The `move()` method ensures that the snake moves forward while maintaining its body structure.

2. Game Loop:
   - The game loop continuously updates the screen and checks for interactions (eating food, colliding with walls, or hitting itself). If a condition ends the game, such as the snake hitting a wall, the game stops, and the score is displayed.

3. Object-Oriented Design:
   - The game is built using three key classes (`Snake`, `Food`, `Scoreboard`), making the code modular and easy to manage. Each class has its own responsibility, and they interact with each other through method calls.


- Level Progression: Increase the speed of the game as the snake gets longer or with each score increase.
- Power-ups: Introduce random food items that grant temporary speed boosts or slow down the game.
- Obstacle Addition: screen four walls are obstacles that the snake must avoid.
- High Score Tracking: Keep track of the highest score across multiple game sessions.
