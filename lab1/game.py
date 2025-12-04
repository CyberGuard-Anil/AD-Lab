import random
options = ["rock","paper","scissor"]

user = input("Enter rock,paper, or scissor : ").lower()

computer = random.choice(options)

print("Your Choice : ",user)
print("Computer Choice : ",computer)

if user == computer:
	print("It's a tie!")
elif (user == "rock" and computer == "scissor") or \
	(user == "paper" and computer == "rock") or \
	(user == "scissor" and computer == "paper"):
	print("You Win!")
else:
	print("Computer Wins!")
