import random

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

moves = [rock, paper, scissors]

lost = "You lose"
won = "You win"

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

pc_choice = random.randint(0,2)

print(f"{moves[player_choice]}\nComputer choose:\n{moves[pc_choice]}")

if player_choice == pc_choice:
    print("It's a draw")
elif player_choice == 0:
    if pc_choice == 1:
        print(lost)
    elif pc_choice == 2:
        print(won)
elif player_choice == 1:
    if pc_choice == 0:
        print(won)
    elif pc_choice == 2:
        print(lost)
elif player_choice == 2:
    if pc_choice == 0:
        print(lost)
    elif pc_choice == 1:
        print(won)