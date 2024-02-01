############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    return random.choice(cards)


def winner(player, dealer):
    if sum(player) > 21:
        print("You went over. You lost.")
    elif sum(dealer) > 21:
        print("Opponent went over. You win 😁")
    elif sum(player) > sum(dealer):
        print("You win 😁")
    elif sum(dealer) > sum(player):
        print("You lost.")
    else:
        print("Draw :/")


def deal():
    for i in range(2):
        hand.append(random_card())
        opponent.append(random_card())


def ace_value(player):
    if 11 in player and sum(player) > 21:
        for i in range(len(player)):
            if player[i] == 11:
                player[i] = 1


keep_running = True

while keep_running:
    hand = []
    opponent = []
    keep_drawing = True

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    deal()

    if start == "y":
        os.system("cls")

        print(logo)

        print(f"Your cards: {hand}, current score: {sum(hand)}")
        print(f"Computer's first card: [{opponent[0]}, ?]")

        if sum(opponent) == 21:
            print("Opponent has blackjack. You Lose!")
            continue

        while keep_drawing:
            ace_value(hand)

            if sum(hand) < 21 and sum(opponent) < 21:
                draw = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                draw = "n"

            if draw == "y":
                hand.append(random_card())
                ace_value(hand)

                print(f"Your cards: {hand}, current score: {sum(hand)}")
                print(f"Computer's first card: [{opponent[0]}, ?]")
            else:
                print(f"Your final hand: {hand}, final score: {sum(hand)}")
                while (
                    sum(opponent) <= sum(hand)
                    and sum(opponent) < 18
                    and sum(hand) <= 21
                ):
                    opponent.append(random_card())

                keep_drawing = False

                print(
                    f"Computer's final hand: {opponent}, final score: {sum(opponent)}"
                )

        winner(hand, opponent)

    else:
        keep_running = False
