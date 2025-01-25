# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from tkinter import *
from tkinter import messagebox

import pyperclip

import password_generator

from pyexpat.errors import messages

FONT =("Arial",14,"bold")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height= 200, bg="white", highlightthickness=0)

my_pass = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=my_pass)
canvas.grid(column=0, columnspan=3, row = 0)


website_label = Label(text="Website:",fg="Black",font=FONT,bg="white",pady=10,padx=10)
website_label.grid(column=0, row = 1)


email_label = Label(text="Email/Username: ",fg="Black",font=FONT,bg="white",pady=10,padx=10)
email_label.grid(column=0, row = 2)


password_label = Label(text="Password: ",fg="Black",font=FONT,bg="white",pady=10,padx=10)
password_label.grid(column=0, row = 3)

# ---------------------------- SAVE PASSWORD ------------------------------- #

website_input = Entry(width=20)
website_input.config(font=FONT)
website_input.grid(column=1, row=1, padx=10, pady=10)
website_input.focus()


email_input = Entry(width=37)
email_input.config(font=FONT)
email_input.grid(column=1, row=2,columnspan=2, padx=10, pady=10)


password_input = Entry(width=20)
password_input.config(font=FONT)
password_input.grid(column=1, row=3, padx=10, pady=10)


def generate_password():
    password = password_generator.generate_password()
    password_input.insert(END, string=password)
    pyperclip.copy(password)

generate_password_button = Button(text="Generate Password", command= generate_password, width= 21 , bg="white",bd=5,relief=RAISED)
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

# ---------------------------- search ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("passwords.json", "r") as passwords_data:
            passwords = json.load(passwords_data)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No Data File Found")
    else:
        if website in passwords:
            data = passwords[website]
            messagebox.showinfo("Password Found",
                                f"The Data for Website {website}:"
                                f"\nUsername: {data['email']}"
                                f"\nPassword: {data['password']}")
        else:
            messagebox.showwarning("Warning", "No Details for the website exist")

search_button = Button(text="Search", command=find_password, width=21, bg="white", bd=5, relief=RAISED)
search_button.grid(column=2, row=1, padx=10, pady=10)



# ---------------------------- UI SETUP ------------------------------- #
def add_password() :
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "" :
        messagebox.showwarning("Warning", "Field is empty! Please Fill all required fields")
    elif len(website) < 3 or len(email) < 3 or len(password) < 3 :
        messagebox.showwarning("Warning", "Input is Too short!")
    else:
        confirmation = messagebox.askokcancel(title=website, message= f"This is the information you entered "
                                                                      f"\nUsername : {email} and password {password} \nIs it okay to save?")
        if confirmation :
            new_data = {
    website : {
        "email": email,
        "password": password
    }
            }
            try :
                with open("passwords.json", "r") as pass_data:
                    data = json.load(pass_data)
                    data.update(new_data)
            except :
                with open("passwords.json", "w") as pass_data:
                    json.dump(new_data,pass_data,indent=4)
            else:
                with open("passwords.json", "w") as pass_data:
                    json.dump(data,pass_data,indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)


add_password_button = Button(text="ADD", command= add_password, width= 36 , bg="white",bd=5,relief=RAISED)
add_password_button.grid(column=1, row=4,columnspan=2, padx=10, pady=10)



window.mainloop()
