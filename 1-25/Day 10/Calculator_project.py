from itertools import repeat


def add(number1, number2):
    add_result = number1 + number2
    return add_result

def subtract(number1, number2):
    subtract_result = number1 - number2
    return subtract_result

def multiply(number1, number2):
    multiply_result = number1 * number2
    return multiply_result

def divide(number1, number2):
    divide_result = number1 / number2
    return divide_result

import art
print(art.logo)
print("Welcome to our calculator App!")


calculator = {}

calculator["+"] = add
calculator["-"] = subtract
calculator["*"] = multiply
calculator["/"] = divide

repeat_flag = True

while repeat_flag :
    second_operation = False
    first_number = input("Please enter the first number you want to use : ")
    if not first_number.isnumeric() :
            print("please enter a valid number")
            continue
    else :
            first_number = float(first_number)
        

    while not second_operation:
        operator  = input("Please enter the mathematical operator you want to use :\n"
                              "(a choice of '+', '-', '*' or '/')")

        if operator not in calculator :
                    print("please enter a valid mathematical operator\n"
                          "(The available choices are '+', '-', '*' or '/')")
                    continue
        else :
            second_number = input("Please enter the Second number you want to use : ")
            if not second_number.isnumeric():
                print("please enter a valid number")
                continue
            else:
                second_number = float(second_number)
                result = calculator[operator](first_number,second_number)

                print(f"**********************************************************\n"
                      f"result of :( {first_number} {operator} {second_number} )= "
                                  f"{result} \n"
                      f"**********************************************************\n")

                another_operation = input(f"Type 'Y' to continue To continue calculating with {result} ,\n "
                                                  "type ‘N’ to start a new calculation,\n ""type ‘E’ to exit calculator ").lower()
                if another_operation == 'y':
                    first_number = result
                    second_operation = False
                elif another_operation == 'n':
                    second_operation = True
                elif another_operation == 'e':
                    repeat_flag = False
                    second_operation = True



