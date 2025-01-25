Day 19 : Event-driven programming : 

In Day 19's project, the focus is on simulating a turtle race using the turtle module in Python. This project introduces interactive elements and randomness, enhancing the understanding of event-driven programming and the use of objects (Turtles) in a graphical context.

Key Concepts Covered:

Turtle Setup and Positioning:
The project involves creating multiple turtle objects, each assigned a unique color and starting position. This demonstrates how to manage multiple objects in a graphical environment.

Screen Setup: The turtle's screen size is configured using screen.setup(width=500, height=400), providing enough space for the race.

User Interaction:
textinput() Function: This function is used to prompt the user to place a bet by selecting the color of the turtle they think will win. This adds interactivity to the program, allowing for dynamic user input and creating an engaging experience.

Creating Multiple Turtle Objects:
The Turtle class is used to create six turtle racers, each assigned a different color from the colors list. These turtles are placed at predefined y-positions to ensure they start on separate tracks.

Race Logic and Movement:
The race starts when the user places a bet.
Random distances are generated for each turtle to simulate variable speed, adding unpredictability to the race.

Checking for the Winner:
As the turtles move forward, their x-coordinate is checked to determine if they've crossed the finish line. Once a turtle crosses, the race ends, and the color of the winning turtle is compared to the user's bet. Depending on the result, a message is printed to inform the user whether they won or lost.

Event-Driven Programming:
This project reinforces event-driven programming concepts, where the race only begins once the user has placed a bet. The turtle race loop is dependent on continuous updates to the turtle's position and user input, giving a real-time feel to the game.

