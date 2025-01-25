
class QuizBrain :
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)



    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q{self.question_number} : {new_question.text} (True/False)? : {new_question.answer}  ")
        result = self.check_answer(user_answer,new_question.answer)
        if result :
            self.score +=1
        print(f"Your Current score is : {self.score}/{self.question_number}")
        print("\n")



    def check_answer(self,user_answer,correct_answer):
        right = False
        if user_answer.lower() == correct_answer.lower() :
            print("Right!")
            right = True
        else:
            print("wrong!")
        print(f"The correct answer was : {correct_answer}")
        return right


