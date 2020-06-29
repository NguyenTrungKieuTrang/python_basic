from random import randint

print("Select Keo, Bua, Bao")
player = input()
computer = randint(0,2)


if computer == 0:
	computer = "Bua"
if computer == 1:
	computer = "Bao"
if computer == 2:
	computer = "Keo"

print("------")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("------")

if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Bua":
			print("You Lose")
		else:
			print("You Win")

	elif player == "Bua":
		if computer == "Bao":
			print("You Lose")
		else:
			print("You Win")

	elif player == "Bao":
		if computer == "Keo":
			print("You Lose")
		else:
			print("You Win")
	else: 
		print("Input Wrong")
