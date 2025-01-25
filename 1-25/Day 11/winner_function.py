
def winner(user_cards,computer_cards) :
    user_score = sum(card for card in user_cards if isinstance(card, int))
    computer_score = sum(card for card in computer_cards if isinstance(card, int))

    if computer_score > user_score:
        print(f"Your final hand: {user_cards}, final score: {user_score}.\n"
              f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Computer Wins! You Lose!")
        repeat_flag = False
    elif user_score > computer_score:
        print(f"Your final hand: {user_cards}, final score: {user_score}.\n"
              f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("YOU Wins!\n"
              "Congratulations!")
        repeat_flag = False
    else:
        print(f"Your final hand: {user_cards}, final score: {user_score}.\n"
              f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("This is a Draw!")
        repeat_flag = False

        return repeat_flag