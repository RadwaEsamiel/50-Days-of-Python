import art
import function
import random
import winner_function
import cards

cards = cards.cards

new_game = True

while new_game :
    opening = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

    if opening == 'y' :
        print(art.logo)

        user_cards = []
        computer_cards = []

        for starters in range(0, 2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        repeat_flag = True

        while repeat_flag :
            user_score, computer_score, end_flag = function.game(computer_cards,user_cards)
            if end_flag :
                repeat_flag = False
                print(f"Your final hand: {user_cards}, final score: {user_score}.\n"
                      f"Computer's final hand: {computer_cards}, final score: {computer_score}")

            else :
                another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()

                if another_card == 'y':
                    user_cards.append(random.choice(cards))
                    continue
                elif another_card == 'n':

                    computer_score = sum(card for card in computer_cards if isinstance(card, int))

                    if computer_score > 16:
                        repeat_flag = winner_function.winner(user_cards, computer_cards)
                    else:
                        while computer_score < 16:
                            computer_cards.append(random.choice(cards))
                            computer_score = sum(card for card in computer_cards if isinstance(card, int))

                        repeat_flag = winner_function.winner(user_cards, computer_cards)
                else:
                    print("Invalid Answer!")
                    continue


    elif opening == 'n':
        new_game = False
    else:
        print('Invalid Answer')
        continue





