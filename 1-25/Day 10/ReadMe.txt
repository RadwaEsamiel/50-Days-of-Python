Day 10: Basic Calculator App

This project implements a basic calculator app where users can perform multiple arithmetic operations: addition, subtraction, multiplication, and division. The program supports continuous calculations using the result of the previous operation, offers a new calculation option, and allows the user to exit the app.

Key Components:

Functions for Arithmetic Operations:
The app defines separate functions for addition, subtraction, multiplication, and division:
add(), subtract(), multiply(), and divide().
Each function takes two numbers as arguments and returns the result of the operation.

Dynamic Operator Handling:
A dictionary, calculator, is used to map mathematical operators (+, -, *, /) to their respective functions. This design allows flexible operator handling.

Input Handling and Validation:
The app prompts the user to enter the first and second numbers and ensures the inputs are numeric.
The operator is also validated to ensure it is one of the supported mathematical symbols.

Loop for Continuous Operation:
The program is structured with a loop that allows the user to either:
Continue calculating with the result of the previous operation.
Start a new calculation.
Exit the calculator.
