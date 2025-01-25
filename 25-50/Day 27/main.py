import tkinter
from tkinter.ttk import Button, Entry

window = tkinter.Tk()
window.title("My First Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

my_label = tkinter.Label(text="label testing",font=("Arial",30,"bold"))
# my_label.pack(side="left")
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New text")

new_button = Button(text="new button")
new_button.grid(column=2, row=0)
new_button.config(padding=20)

def button_action():
    print("i got clicked")
    user_input = input.get()
    my_label.config(text=user_input)


button = Button(text="click",command=button_action)
button.grid(column=1, row=1)

input = Entry(width=20)
# input.place(x=200,y=200)
input.grid(column=3, row=2)




window.mainloop()