# Joe Peak
# CS101L Section 004
# 9/14/22

print("Welcome to Flarsheim Guesser!\n")

# Variable to break / continue game loop
game_over = False

while(game_over == False):

	print("Please think of a number between and including 1 and 100.\n")

	# Get user number modulo 3
	three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))
	# Keep prompting until valid input
	while(three_remainder < 0 or three_remainder > 2):
		if(three_remainder < 0):
			print("The value entered must be 0 or greater.")
			three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))
		else:
			print("The value entered must be less than 3")
			three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))

	# Get user number modulo 5
	five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))
	# Keep prompting until valid input
	while(five_remainder < 0 or five_remainder > 4):
		if(five_remainder < 0):
			print("The value entered must be 0 or greater.")
			five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))
		else:
			print("The value entered must be less than 5")
			five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))

	# Get user number modulo 7
	seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))
	# Keep prompting until valid input
	while(seven_remainder < 0 or seven_remainder > 6):
		if(seven_remainder < 0):
			print("The value entered must be 0 or greater.")
			seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))
		else:
			print("The value entered must be less than 7")
			seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))

	# Check each value from 1 - 100
	for i in range(1, 101):
		if((i % 3 == three_remainder) and (i % 5 == five_remainder) and (i % 7 == seven_remainder)):
			print(f"Your number was {i}")
			print("How amazing is that?\n")
			break

	# Ask user to play again
	play_again = input("Do you want to play again? Y to continue, N to quit ==> ")

	# Keep prompting for valid input
	while(play_again != 'Y' or play_again != 'N'):
		if(play_again == 'Y'):
			game_over = False
			break
		elif(play_again == 'N'):
			# End game
			game_over = True
			break
		else:
			play_again = input("Do you want to play again? Y to continue, N to quit ==> ")
