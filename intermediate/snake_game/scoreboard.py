import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.teleport(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def eat(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
