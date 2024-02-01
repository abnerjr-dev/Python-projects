import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

keep_running = True
bidders = {}

while keep_running:
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[bidder] = bid

    another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if another_bid == "yes":
        os.system("cls")
        pass
    else:
        keep_running = False
        winner = ""
        win_bid = 0
        for person in bidders:
            if bidders[person] > win_bid:
                win_bid = bidders[person]
                winner = person

        print(f"The winner is {winner} with a bid of ${win_bid}")
