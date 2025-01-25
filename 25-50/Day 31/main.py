from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

# Set up the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create the canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = PhotoImage(file=r".\images\card_front.png")
flipped_card = PhotoImage(file=r".\images\card_back.png")
card_img = canvas.create_image(400, 263, image=flash_card)  # Center the image (400,263 is the center)
canvas.grid(column=0, columnspan=2 , row=0, padx=10, pady=10)

# read csv data
try :
    words_to_learn = pd.read_csv(r"./data/words_to_learn.csv")
    words_dict = words_to_learn.set_index("English Translation")["Arabic Word"].to_dict()
except FileNotFoundError :
    data = pd.read_csv(r"./data/arabic_words.csv")
    words_dict = data.set_index("English Translation")["Arabic Word"].to_dict()


random_key_word = random.choice(list(words_dict.keys()))
random_arabic_word = words_dict[random_key_word]
flipping = ""
score = 0
rep = 0

# Create text on the canvas
language_text = canvas.create_text(400, 150, text="Arabic", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 265, text=random_arabic_word, font=("Arial", 60, "bold"), fill="black")
score_text = canvas.create_text(400, 380, text=f"{score}/{rep}", font=("Arial", 40, "bold"), fill="black")

def show_new_word():
    global rep
    rep += 1
    canvas.itemconfig(card_img, image=flash_card)
    global random_arabic_word,random_key_word
    random_key_word = random.choice(list(words_dict.keys()))
    random_arabic_word = words_dict[random_key_word]

    canvas.itemconfig(word_text, text=random_arabic_word, fill="black")
    canvas.itemconfig(language_text, text="Arabic", fill="black")
    update_score_text()
    # Show the word for 5 seconds, then flip to English
    global flipping
    flipping = window.after(5000, delayed_flip_card, random_arabic_word)


def save_words_to_learn():
    # Save remaining words to words_to_learn.csv
    df = pd.DataFrame(words_dict.items(), columns=["Arabic Word", "English Translation"])
    df.to_csv(r"./data/words_to_learn.csv", index=False)


# Create wrong answer button
def wrong_answer():
    if canvas.itemcget(language_text, "text") == "Arabic" :
        window.after_cancel(flipping)
        answered_flip_card(random_arabic_word)


wrong_answer_image = PhotoImage(file=r".\images\wrong.png")
wrong_answer_button = Button(image=wrong_answer_image, highlightthickness=0, relief="flat",bg=BACKGROUND_COLOR, command= wrong_answer)
wrong_answer_button.grid(column=0, row=1, padx=10, pady=10)

# Create wrong right button
def right_answer():
    words_dict.pop(random_key_word)
    save_words_to_learn()
    if canvas.itemcget(language_text, "text") == "Arabic" :
        global score
        score += 1
        window.after_cancel(flipping)
        answered_flip_card(random_arabic_word)


right_answer_image = PhotoImage(file=r".\images\right.png")
right_answer_button = Button(image=right_answer_image, highlightthickness=0, relief="flat",bg=BACKGROUND_COLOR, command= right_answer)
right_answer_button.grid(column=1, row=1, padx=10, pady=10)



def update_score_text():
    canvas.itemconfig(score_text, text=f"{score}/{rep}")


def delayed_flip_card(word):
    canvas.itemconfig(card_img, image=flipped_card)
    canvas.itemconfig(language_text, text="English", fill="white")

    canvas.itemconfig(word_text, text=random_key_word, fill="white")
    window.after(3000, show_next_word)

def show_next_word():
    # Show a new word after flipping
    show_new_word()

def answered_flip_card(word):
    canvas.itemconfig(card_img, image=flipped_card)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_key_word, fill="white")
    window.after(2000, show_next_word)


show_new_word()


window.mainloop()
