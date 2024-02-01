import art
from game_data import data
import os
import random


def chose_comp():
    return random.choice(data)


def introduce(personA, personB):
    print(
        f'compare A: {personA["name"]}, a {personA["description"]} from {personA["country"]}'
    )
    print(art.vs)
    print(
        f'Against B: {personB["name"]}, a {personB["description"]} from {personB["country"]}'
    )


def winner(personA, personB):
    if personA["follower_count"] > personB["follower_count"]:
        return "A"
    else:
        return "B"


keep_playing = True

while keep_playing:
    keep_running = True
    A = chose_comp()
    B = chose_comp()
    while A == B:
        B = chose_comp()

    score = 0

    start = input(
        "\nWould you like to play a game of Higher or Lower? Type 'y' or 'n': "
    ).lower()

    if start == "y":
        while keep_running:
            os.system("cls")

            print(art.logo)
            if score != 0:
                print(f"you are right! current score: {score}")
            introduce(A, B)

            guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()

            if guess == winner(A, B):
                A = B
                B = chose_comp()
                while A == B:
                    B = chose_comp()
                score += 1

            else:
                os.system("cls")
                print(art.logo)
                print(f"Sorry that's wrong. Final Score: {score}")
                keep_running = False

    else:
        keep_playing = False
