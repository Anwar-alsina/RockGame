# Write your solution below the starter code
# Follow the instructions in the tab to the right

# Starter code - no need to edit
import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")
text = ("You have to enter Rock, Paper, or Scissors? ")
choice = input("Rock, Paper, or Scissors? ")

# Make a choice for the computer player
random_value = random.randint(1,3)
computer_choice = random.randint(1, 3)
if random_value == 1:
  computer_choice = "Rock"
elif random_value == 2:
  computer_choice = "Paper"
elif random_value == 3:
  computer_choice = "Scissors"
else:
  print("Something went wrong with RANDOM")

print("The computer chooses " + computer_choice )

# Add the rest of the game code here
if choice == computer_choice:
    print(choice,"and", computer_choice + " It's a draw.")
elif choice == "Rock":
    if computer_choice == "Scissors":
        print("Rock smashes Scissors. You win!")
    else:
        print("Paper covers Rock. You lose!")
elif choice == "Paper":
    if computer_choice == "Rock":
        print("Paper covers Rock. You win!")
    else:
        print("Scissors cut Paper. You lose!")
elif choice == "Scissors":
    if computer_choice == "Paper":
        print("Scissors cut Paper. You win!")
    else:
        print("Rock smashes Scissors. You lose!")
else:
  print(text)
    