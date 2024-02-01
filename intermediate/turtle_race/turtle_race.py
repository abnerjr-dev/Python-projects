from turtle import Turtle, Screen
import random as r


race_on = False
screen = Screen()
screen.setup(width=532, height=800)

background = "intermediate/turtle_race/turtle_racetrack_2.png"
screen.bgpic(background)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
r.shuffle(colors)
turtles = []

y = -350

for t in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(f"{t}")
    new_turtle.penup()

    new_turtle.goto(-250, y)
    turtles.append(new_turtle)
    y += 140

player_count = int(screen.textinput("how many players", "How many people are betting?"))

players = []
for player in range(player_count):
    user_name = screen.textinput(
        f"Player {len(players) + 1}", "Please enter your name."
    )
    user_bet = screen.textinput(
        f"Make your bet {user_name}", "Which turtle will win the race? Enter a color."
    )
    player_info = [user_name, user_bet]
    players.append(player_info)

if players:
    race_on = True

winner = False

while race_on:
    for t in turtles:
        step = r.randint(0, 10)
        t.forward(step)

        if t.xcor() > 240:
            race_on = False
            print(f"The {t.color()[0].title()} Turtle has won!")
            winning_color = t.color()[0]
            for player in players:
                if player[1] == winning_color:
                    print(f"{player[0]} won the bet!")
                    winner = True
            break
if not winner:
    print("You lost all your money...")

screen.exitonclick()
