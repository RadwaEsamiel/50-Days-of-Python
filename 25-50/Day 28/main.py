import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row = 1)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer_label.grid(column=1, row = 0)

def reset_timer() :
    print("i was clicked")
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global rep
    rep = 0

reset_button = Button(text="Reset", command= reset_timer)
reset_button.grid(column=2, row = 2)


def start_timer() :
    print("i was clicked")
    global rep
    rep += 1

    if rep in(1,3,5,7) :
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK MINUTES",fg=GREEN)
    if rep in(2,4,6) :
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="SHORT BREAK MINUTES",fg=PINK)
    if rep == 8 :
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="LONG BREAK MINUTES",fg=RED)

start_button = Button(text="Start", command= start_timer)
start_button.grid(column=0, row = 2)

check_mark = Label(text="✔",font=(FONT_NAME, 20, "bold"), fg=GREEN, bg= YELLOW)
check_mark.grid(column=1, row = 3)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count%60
    if seconds < 10 :
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0 :
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

        check_marks_string = ""
        if rep % 2 == 0 :
            check_marks = math.floor(rep / 2)
            for cm in range(check_marks) :
                check_marks_string += "✔"
                check_mark.config(text=check_marks_string)


# ---------------------------- UI SETUP ------------------------------- #




window.mainloop()