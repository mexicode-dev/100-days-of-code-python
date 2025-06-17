import random

# ASCII art for Rock, Paper, and Scissors
rock =  """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Store ASCII art in a list for easy access
game_images = [rock, paper, scissors]

# Get user's choice as an integer (0 - Rock, 1 - Paper, 2 - Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

# Check if the user_choice is valid and print the selected image
if 0 <= user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You typed an invalid number. You lose!")
    # Exit the program early if input is invalid
    exit()

# Generate computer's choice (randomly between 0 and 2)
computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    # Scissors loses to Rock
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You lose!")