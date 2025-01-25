def calculate_love_score(first_name, second_name):

    true_letters = list("true")
    love_letters = list("love")


    true_counter = 0
    love_counter = 0


    for letter in first_name :
        if letter in true_letters :
            true_counter += 1
        if letter in love_letters :
            love_counter += 1

    for letter in second_name :
        if letter in love_letters :
            love_counter += 1
        if letter in true_letters :
            true_counter += 1

    print(f"love score is : {true_counter}{love_counter}")




calculate_love_score("Kanye West", "Kim Kardashian")

