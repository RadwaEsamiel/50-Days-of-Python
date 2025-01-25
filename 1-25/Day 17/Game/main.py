from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


data_len = len(question_data)
question_bank=[]
for text in range(data_len) :
    dicts = question_data[text]
    new_question = Question(dicts['text'],dicts['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions() :
    quiz.next_question()
    if not quiz.still_has_questions() :
        print("You have completed the quiz")
        print(f"your final score was : {quiz.score}/{quiz.question_number}")
        break




