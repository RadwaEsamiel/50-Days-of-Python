Day 17 : quiz game : 
In Day 17's project, the main focus is on reinforcing the concepts of Object-Oriented Programming (OOP), specifically through creating a quiz game that handles questions and tracks the user's progress.

Key OOP Concepts in this Project:

Class Definitions:
Two primary classes are created: Question and QuizBrain.
The Question class is simple and represents individual questions, holding both the question text and the correct answer.
The QuizBrain class handles the core logic of the quiz, including asking questions, keeping track of the score, and determining if there are more questions left.

Encapsulation:
The data and behavior of each question (text and answer) are encapsulated within the Question class. This allows the QuizBrain class to interact with Question objects without worrying about the internal representation of each question.
Similarly, the QuizBrain class encapsulates all logic related to managing the quiz—tracking question numbers, user responses, and calculating scores.

Abstraction:
The QuizBrain class abstracts away the complexity of interacting with the quiz data. The main program doesn’t need to know the details of how questions are stored or how the score is calculated. Instead, the program can rely on methods like next_question() and still_has_questions() to manage the quiz flow.
This means the user interacts with simple and clear methods, without having to deal with the underlying logic of question handling and answer checking.

Modularity:
The Question and QuizBrain classes are independent modules. This modularity makes the code more organized and easier to maintain. If you wanted to update how questions are managed, you could modify the Question class without affecting the quiz logic in QuizBrain.
Similarly, the quiz logic could be updated or extended without touching the way individual questions are defined or stored.

Reusability:
The project demonstrates how code can be reused by breaking it down into meaningful objects. The Question class, for instance, can be used anywhere a question/answer pair is needed, beyond just this quiz game.
The QuizBrain class could also be easily extended to handle more advanced quizzes (e.g., adding different question types, allowing multiple choice, etc.).

Control Flow:
The QuizBrain class contains the logic to move through the quiz using methods like next_question() and check_answer(). This class also controls the flow of the quiz using loops and conditionals (e.g., checking if there are more questions, updating the score based on user answers).

Data Processing:
The quiz is based on a collection of dictionaries (question_data), and the Question class is used to transform that data into objects that the quiz can use. This is a good example of how OOP can be used to process and manage data in a more structured and flexible way.