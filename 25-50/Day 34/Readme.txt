Day 34 : Quiz Application with GUI :
This project is a Quiz Application built with Python, utilizing the Tkinter library for a user-friendly graphical interface. The application integrates with the Open Trivia Database API to fetch trivia questions, making each quiz dynamic and unique. The project demonstrates the integration of API-driven content with GUI components, providing an interactive quiz experience.

Project Overview

Class Structure and Quiz Logic:

The application is structured around three main classes: Question, QuizBrain, and QuizInterface.
Question stores each question and its answer.
QuizBrain handles the quiz flow, question tracking, and scoring, as well as checking if the user’s response is correct.
QuizInterface builds the graphical interface, presenting questions to the user, managing the score display, and updating visuals based on answers.

Fetching Questions from an API:
Trivia questions are fetched from the Open Trivia Database API in real time, based on parameters such as difficulty level and question type. The API response is processed to create question instances that are loaded into the quiz.

GUI with Tkinter:
The interface is designed with Tkinter, featuring a label to display the score, a canvas for the questions, and buttons for user interaction. True/False buttons allow users to submit answers, and the canvas changes color to indicate whether an answer was correct or incorrect.

Dynamic Question Loading and Scoring:
The application dynamically loads each question, updating the display and score based on user responses. Once all questions are answered, the app disables the answer buttons and displays a completion message.
