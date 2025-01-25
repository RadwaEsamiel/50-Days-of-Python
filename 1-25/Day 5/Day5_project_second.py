letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


import random

loop_choice_list = []
for letters_number in range(1,5) :
    loop_choice_list += random.choice(letters)

for numbers_number in range(1,5) :
    loop_choice_list += random.choice(numbers)

for symbols_number in range(1,5) :
    loop_choice_list += random.choice(symbols)

random.shuffle(loop_choice_list)


password = ""
for password_number in loop_choice_list :
    password += random.choice(loop_choice_list)


print(f"your password is : {password}")


