print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S" :
    print("The price for small pizza is $15")
    bill += 15
    if pepperoni == "Y" :
        bill +=2
        print("The price for Extra pepperoni on small pizza is $2")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")

    elif pepperoni == "N" :
        print("No Extra pepperoni")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")
    else :
        print("Invalid choice please type Y for yes and N for no .")

elif size == "M" :
    print("The price for Medium  pizza is $20")
    bill += 20
    if pepperoni == "Y" :
        bill +=3
        print("The price for Extra pepperoni on Medium pizza is $3")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")
    elif pepperoni == "N" :
        print("No Extra pepperoni")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")
    else :
        print("Invalid choice please type Y for yes and N for no .")

elif size == "L" :
    print("The price for Large pizza is $25")
    bill += 25
    if pepperoni == "Y" :
        bill +=3
        print("The price for Extra pepperoni on Large pizza is $3")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")
    elif pepperoni == "N" :
        print("No Extra pepperoni")
        if extra_cheese == "Y":
            print("The price for Extra Cheese is $1")
            bill += 1
        elif extra_cheese == "N":
            print("No Extra Cheese")
        else:
            print("Invalid choice please type Y for yes and N for no .")
    else :
        print("Invalid choice please type Y for yes and N for no .")



else :
    print("Invalid Size please type S, M or L.")

print(f"Your total bill amount is : {bill}")


_______________________________________________________________________________
_______________________________________________________________________________

_______________________________________________________________________________
_______________________________________________________________________________


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S" :
    print("The price for small pizza is $15")
    bill += 15

elif size == "M" :
    print("The price for Medium  pizza is $20")
    bill += 20

elif size == "L" :
    print("The price for Large pizza is $25")
    bill += 25
else :
    print("Invalid Size please type S, M or L.")

if pepperoni == "Y" :
    if size == "S":
        bill +=2
        print("The price for Extra pepperoni on small pizza is $2")
    elif size == "M" :
        bill += 3
        print("The price for Extra pepperoni on Medium pizza is $3")
    elif size == "L" :
        bill += 3
        print("The price for Extra pepperoni on Large pizza is $3")

elif pepperoni == "N" :
    print("No Extra pepperoni")
else:
    print("Invalid choice please type Y for yes and N for no .")

if extra_cheese == "Y":
    print("The price for Extra Cheese is $1")
    bill += 1
elif extra_cheese == "N":
    print("No Extra Cheese")
else:
    print("Invalid choice please type Y for yes and N for no .")

print(f"Your total bill amount is : {bill}")
