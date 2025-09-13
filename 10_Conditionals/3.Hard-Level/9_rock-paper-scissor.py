# Implement a rock-paper-scissor game

import random

choices = ["rock", "paper", "scissor"]
user = input("Enter your choice(rock, paper, scissor): ").lower()
computer = random.choice(choices)
print("Computer chose:", computer)

if user == computer:
    print("it's tie!")
elif (user == "rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")