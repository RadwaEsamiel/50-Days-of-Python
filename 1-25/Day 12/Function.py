import random

def guess_game(attempts) :
    end_guess = False
    number = random.choice(range(1,101))
    print(number)


    while not end_guess :
        guess = input("Make a Guess : ")
        attempts -= 1

        if attempts == 0 :
            print("Wrong Guess! You've run out of guesses, you lose.")
            end_guess = True
        else :
            if not guess.isnumeric() :
                print("Please enter a valid number!")
            elif int(guess) > 100 :
                print("Number is between 1 and 100!")
            else:
                if int(guess)-number > 0 :
                    print(f"You have {attempts} more attempts remaining to guess the number.")
                    print("Too High\n"
                          "Guess Again")
                    continue
                elif int(guess)-number < 0 :
                    print(f"You have {attempts} more attempts remaining to guess the number.")
                    print("Too Law\n"
                          "Guess Again")
                    continue
                elif int(guess)-number == 0 :
                    print(f"You got it! The answer was {number}")
                    end_guess = True

    return end_guess
