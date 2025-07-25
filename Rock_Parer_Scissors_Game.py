import random

rock = '''
    _-------
---'    ____)
       (_____)
       (_____)
       (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)__
         _____)
        ______)
         ____)
 ---.__(___)
 '''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# --- Input Validation (Moved to the beginning) ---
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # --- Game Logic ---
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")