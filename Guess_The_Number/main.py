import random
import art

def guessing_game(attempt_count):
	number = random.randint(1, 100)
	#print(f"number is {number}")
	while attempt_count > 0 :
		print(f"You have {attempt_count} attempts to guess the number.")
		user_guess = int(input("Make a guess: "))
		if user_guess == number:
			print(f" Great..!! You guessed the correct number! The answer was {number}.")
			break
		elif user_guess > number:
			attempt_count -= 1
			if attempt_count > 0:
				print("Your guess is Too High.\n Make a Guess again.")
			else:
				print("You ran out of guesses.")
				break

		elif user_guess < number:
			attempt_count -= 1
			if attempt_count > 0:
				print("Your guess is Too low.\n Make a Guess again.")
			else:
				print("You ran out of guesses.")
				break

		else:
			print(f"You have {attempt_count} attempts to guess the number.")

	if attempt_count == 0 or user_guess == number:
		print("Kindly restart the game....Best of luck.!!")




def main():
	print(art.logo)
	print("Welcome to the number guessing game..!! \nI'm thinking of a number between 1 and 100.You will try to guess the number")
	choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if choice.lower() == "easy":
		guessing_game(10)
	elif choice.lower() == "hard":
		guessing_game(5)
	else:
		print("Wrong choice. Sorry, start again.")


main()