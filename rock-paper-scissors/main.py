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
---'   ____)_______
          _________)
          __________)
         __________)
---._____________)
'''

scissors = '''
    _______
---'   ____)_______
          _________)
       ___________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an Invalid Number, You Lose!")
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"\nComputer chose:\n")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You Win!")
        elif user_choice == 2 and computer_choice == 0:
            print("The Computer Wins!")
        elif user_choice == computer_choice:
            print("It's a Draw!")
        elif user_choice == 2 and computer_choice == 0:
            print("You Lose!")
        elif user_choice < computer_choice:
            print("You Lose!")
        elif user_choice > computer_choice:
            print("You Win!")
except ValueError:
    print("That's not a number! You Lose!")
