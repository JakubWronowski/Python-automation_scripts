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

print("Welcome to Rock, Paper, Scissors game!")
list_of_choices = [rock, paper, scissors]

players_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n "))

computers_choice = random.choice(list_of_choices)

rock_choice = list_of_choices[0]
paper_choice = list_of_choices[1]
scissors_choice = list_of_choices[2]

print("You choose:")
if players_choice == 0:
    print(rock_choice)
    print(f"Computer choosed:\n {computers_choice}")
    if computers_choice == paper_choice:
        print("Computer wins...")
    elif computers_choice == rock_choice:
        print("It's a tie")
    else:
        print("You win!")
elif players_choice == 1:
    print(paper_choice)
    print(f"Computer choosed:\n {computers_choice}")
    if computers_choice == scissors_choice:
        print("Computer wins...")
    elif computers_choice == paper_choice:
        print("It's a tie")
    else:
        print("You win!")
elif players_choice == 2:
    print(scissors_choice)
    print(f"Computer choosed:\n {computers_choice}")
    if computers_choice == rock_choice:
        print("Computer wins...")
    elif computers_choice == scissors_choice:
        print("It's a tie!")
    else:
        print("You win!")
