from tkinter import *
import tkinter.font as tkf

window = Tk()
window.title("My First Program")
window.minsize(width=400,height=200)
window.config(padx=30,pady=30, bg="white")

default_font = tkf.Font(family="Tahoma", size=16, weight="bold")
window.option_add("*Font", default_font)


window.title("@Miles to KM Converter@")

user_input = Entry(width=10)
user_input.config(font=("Tahoma", 14))
user_input.insert(END, string="0")
user_input.grid(column=1, row=0, padx=10, pady=10)

miles_label = Label(text="Miles",font=("Tahoma", 14), bg="white")
miles_label.grid(column=2, row=0, padx=20, pady=20)

km_label = Label(text="Km",font=("Tahoma", 14), bg="white")
km_label.grid(column=2, row=1, padx=10, pady=10)

equal_label = Label(text="is equal to",font=("Tahoma", 14), bg="white")
equal_label.grid(column=0, row=1, padx=10, pady=10)

output_label = Label(text="0",font=("Tahoma", 14), bg="white")
output_label.grid(column=1, row=1, padx=10, pady=10)


def calculate_action() :
    print("i got clicked")
    user_input_get = float(user_input.get())
    output_km = round(user_input_get * 1.609)

    output_label.config(text=f"{output_km}")


calc_button = Button(
    text="Calculate",
    width= 8,
    height= 1,
    command=calculate_action,
    fg="black",           # White text
    padx=5, pady=5,     # Internal padding to make the button larger
    bd=5,                 # Border width for 3D effect
    relief=RAISED,        # Raised button effect
    cursor="hand2"        # Change cursor to hand when hovering over button
)
calc_button.grid(column=1, row=2, padx=10, pady=10)






window.mainloop()