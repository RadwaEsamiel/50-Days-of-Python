import game_data
import random
import art

def higher_lower_game() :

    last_index = len(game_data.data) - 1
    index_a = random.choice(range(0, last_index))
    compare_a = game_data.data[index_a]
    repeat_flag = True
    score = 0

    while repeat_flag :
        index_b = random.choice(range(0,last_index))
        compare_b = game_data.data[index_b]


        if compare_a['follower_count'] > compare_b['follower_count'] : right_answer = 'a'
        else : right_answer = 'b'

        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, From {compare_a['country']}.")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, {compare_b['description']}, From {compare_b['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B':").lower()

        if answer not in ('a','b') :
            print("Invalid Answer! Please choose either 'A' or 'B'")
            continue
        if answer == right_answer :

            compare_a = compare_b
            score += 1

            print(f"You're right! Current score: {score}")

        else :
            print(f"You're Wrong! GAME OVER! Final score : {score}")
            repeat_flag = False