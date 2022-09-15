import random

print("Welcome to Flarsheim Guesser!\n")
print("Please think of a number between and including 1 and 100.\n")

three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))
while(three_remainder < 0 or three_remainder > 2):
	if(three_remainder < 0):
		print("The value entered must be 0 or greater.")
		three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))
	else:
		print("The value entered must be less than 3")
		three_remainder = int(input("What is the remainder when your number is divided by 3 ? "))

five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))
while(five_remainder < 0 or five_remainder > 4):
	if(five_remainder < 0):
		print("The value entered must be 0 or greater.")
		five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))
	else:
		print("The value entered must be less than 5")
		five_remainder = int(input("What is the remainder when your number is divided by 5 ? "))

seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))
while(seven_remainder < 0 or seven_remainder > 6):
	if(seven_remainder < 0):
		print("The value entered must be 0 or greater.")
		seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))
	else:
		print("The value entered must be less than 7")
		seven_remainder = int(input("What is the remainder when your number is divided by 7 ? "))

for i in range(101):
	if((i % 3 == three_remainder) and (i % 5 == five_remainder) and (i % 7 == seven_remainder)):
		print(f"Your number was {i}")
		break
	else:
		print("No match found.")
		break