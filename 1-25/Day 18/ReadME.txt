Day 18 : graphics in Python : 

In Day 18's project, the focus shifts to working with graphics in Python using the turtle library and experimenting with randomness and color extraction from an image. This project adds an artistic layer to programming by using turtle graphics to generate a grid of colored dots.

Key Concepts Learned:

Using External Libraries:
The project makes use of the colorgram library to extract colors from an image. The extracted colors are then used to create a color palette (color_pal) that is used in turtle graphics.

Turtle Graphics:
Turtle is a graphical module in Python used for drawing shapes, patterns, and other visuals.

Working with Color:
After extracting a list of RGB color tuples using colorgram.extract(), the project demonstrates how to manipulate and use colors with the turtle library. The turtle color mode is set to RGB using turtle.colormode(255) to support custom RGB values.

Randomization:
random.choice() is used to randomly select a color from the extracted palette for each dot. This introduces randomness in the color pattern, creating a visually appealing effect.

Control Flow with Loops:
A for loop is used to iterate over the number of dots (number_of_dots). The turtle draws a dot, moves forward, and when it reaches the end of a row, it moves down and starts a new row. This grid-like structure is accomplished by adjusting the turtle’s direction after drawing a certain number of dots.

Turtle Positioning:
The penup() method is used to move the turtle without drawing lines. After drawing each dot, the turtle moves to the next position using forward() and changes direction when the end of a row is reached.
goto() Method: The turtle is initially positioned at (-300, 300) to ensure that the drawing begins in the top-left corner of the screen.

Modularity and Reusability:
The code is written in a modular way, with configurable parameters like number_of_dots, dots_per_row, dot_size, and spacing. This allows you to easily adjust the appearance of the drawing by changing these values without altering the underlying logic.

Event-Driven Programming:
screen.exitonclick() ensures that the turtle graphics window remains open until a user clicks on it. This introduces a basic form of event-driven programming, where the program waits for user interaction before closing.