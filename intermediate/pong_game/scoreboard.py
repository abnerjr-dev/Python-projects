from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
