import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print(
    "------------------------------------------------------------------------------------------------------------"
)

images = [rock, paper, scissors]

print("Lets play rock, paper, scissors!")
player = int(
    input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors!\n")
)

if player >= 3 or player < 0:
    print("Invalid input. You Lose")
else:
    print(images[player])

    com = random.randint(0, 2)

    print("Computer chose:")

    print(images[com])

    if player == com:
        print("Its a tie:/")
    elif player == 0 and com == 1:
        print("You lose :(")
    elif player == 0 and com == 2:
        print("You win!")

    elif player == 1 and com == 2:
        print("You lose:(")
    elif player == 1 and com == 0:
        print("You win!")

    elif player == 2 and com == 0:
        print("You lose :(")
    elif player == 2 and com == 1:
        print("You win!")
