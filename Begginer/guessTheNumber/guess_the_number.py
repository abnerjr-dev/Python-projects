from art import logo
import random
import os

os.system("cls")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

com_num = random.randint(1, 100)

# print(f"Pssst, the correct answer is {com_num}")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if diff == "easy":
    tries = 10
else:
    tries = 5

keep_running = True

while keep_running:
    print(f"You have {tries} attempts remaining to guess the number.")

    if tries > 0:
        guess = int(input("Make a Guess: "))

        if guess == com_num:
            keep_running = False
            print("You win!")
        elif guess > com_num:
            tries -= 1
            print("Too High.\nTry Again.")
        else:
            tries -= 1
            print("Too Low.\nTry Again.")

    else:
        keep_running = False
        print(f"Out of tries. Better luck next time! The number was {com_num}")
