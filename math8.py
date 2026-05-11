import random

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)

user = input("Enter rock, paper or scissor: ")

print("Computer chose:", computer)

if user == computer:
    print("Draw")

elif (user == "rock" and computer == "scissor") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissor" and computer == "paper"):
    print("You Win")

else:
    print("Computer Wins")