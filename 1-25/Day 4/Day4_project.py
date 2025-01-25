rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



import random

rock_paper_scissors = [rock,paper,scissors]
random_number = random.randint(0, len(rock_paper_scissors)-1)

computer_choice = rock_paper_scissors[random_number]

user_choice = int(input("What do you choose?\n Type 0 for rock, 1 for paper and 2 for scissors!\n"))

if user_choice >=0 and user_choice <= 2 :
    print("The computer Chooses: " + computer_choice)
    print("Your Choice is: " + rock_paper_scissors[user_choice])

    if user_choice == 0 and random_number == 2 :
        print("You Win!")
    elif user_choice == 2 and random_number == 0 :
        print("You Lose!")
    elif user_choice == 2 and random_number == 1 :
        print("You Win!")
    elif user_choice == 1 and random_number == 2 :
        print("You Lose!")
    elif user_choice == 1 and random_number == 0 :
        print("You Win!")
    elif user_choice == 0 and random_number == 1 :
        print("You Lose!")
    elif user_choice == random_number :
        print("This is a draw!")
else:
    print("The computer Chooses: " + computer_choice)
    print("Invalid number entered!\nYou Lose!")