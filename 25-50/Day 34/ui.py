THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0 ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row = 0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1,columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="question", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        true_img = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image=true_img,highlightthickness=0,command= self.true_answer)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image=false_img,highlightthickness=0 ,command= self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()





        self.window.mainloop()


    def true_answer(self):
        answer = self.quiz.check_answer("True")
        self.is_right_wrong(answer)


    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.is_right_wrong(answer)

    def is_right_wrong(self, answer):
        if answer :
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question )



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score : {self.quiz.score}")
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_txt)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've reached the End of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

