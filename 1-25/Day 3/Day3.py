print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120 :
    print("you can ride the rollercoaster ")
else:
    print("sorry you can't ride rollercoaster")

_________________________________<IF Statement>______________________________________

x = int(input("what is the number you want to check?\n"))

if x % 2 == 0 :
    print("Even number")
else :
    print("Odd number")




_______________________<nested IF>__________________________________________


print("Welcome to the rollercoaster!")
height = int(input("please enter you height in CM: "))

if height >= 120 :
    print("you can ride the rollercoaster ")
    age = int(input("please enter your age in years : "))
    if age <= 5 :
        print("you have to pay 2$")
    elif age <= 7 :
        print("you have to pay 5$")
    elif age <= 12 :
        print("you have to pay 10$")
    else :
        print("you have to pay 12$")
else:
    print("sorry you can't ride rollercoaster")


_________________________________________________________________________________


print("Welcome to the rollercoaster!")
height = int(input("please enter you height in CM: "))

if height >= 120 :
    print("you can ride the rollercoaster ")
    age = int(input("please enter your age in years : "))
    if age <= 5 :
        bill = 2
        print("you have to pay 2$")
    elif age <= 7 :
        bill = 5
        print("you have to pay 5$")
    elif age <= 12 :
        bill = 10
        print("you have to pay 10$")
    elif age <= 55 and age >= 45 :
        bill = 0
        print("you can ride for free")
    else :
        bill = 12
        print("you have to pay 12$")

    photo_check = input("Do you want a photo taken? \nplease inter y for yes and n for no ")
    if photo_check == "y" :
        bill += 5
        print(f"your total bill amount is :${bill}")
    else :
        print(f"your total bill amount is :${bill}")

else:
    print("sorry you can't ride rollercoaster")


________________________________________________________________________



