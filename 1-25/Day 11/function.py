import random
import cards

cards = cards.cards


def game(computer_cards, user_cards):
    ace = 'A'
    black_jacks = ['J', 'Q', 'K']
    game_over = False
    computer_score = 0
    user_score = 0


    for bj in black_jacks:
        if bj in computer_cards:
            if ace in computer_cards:
                print("Computer has a blackjack! Computer Wins!\n"
                  "GAME OVER ")
                game_over = True
            else:
                bj_index = computer_cards.index(bj)
                computer_cards[bj_index] = 10

        elif bj in user_cards:
            if ace in user_cards:
                print("You have a blackjack! YOU Wins!\n"
                         "Congratulations!")
                game_over = True

        if bj in user_cards:
            bj_index = user_cards.index(bj)
            user_cards[bj_index] = 10

    if ace in user_cards:
        ace_index = user_cards.index(ace)
        if (user_score + 11) > 21:
             user_cards[ace_index] = 1
        else:
            user_cards[ace_index] = 11


    elif ace in computer_cards:
        ace_index = computer_cards.index(ace)
        if (computer_score + 11) > 21:
            computer_cards[ace_index] = 1
        else:
            computer_cards[ace_index] = 11

    user_score = sum(card for card in user_cards if isinstance(card, int))
    computer_score = sum(card for card in computer_cards if isinstance(card, int))

    if user_score > 21:
        print(f"You Went over! Your score is {user_score} YOU Lose!")
        game_over = True
    else:
        print(f"Your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")

    return user_score, computer_score, game_over



