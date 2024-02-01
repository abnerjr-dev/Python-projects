from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.write(f"Level: {self.score + 1}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score + 1}", align=ALIGNMENT, font=FONT)
