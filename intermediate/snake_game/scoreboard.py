import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("intermediate/snake_game/data.txt", mode="r") as self.file:
            self.high_score = int(self.file.read())

        self.hideturtle()
        self.teleport(0, 270)
        self.color("white")
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("intermediate/snake_game/data.txt", mode="w") as self.file:
                self.file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}     High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def eat(self):
        self.score += 1
        self.update_scoreboard()
