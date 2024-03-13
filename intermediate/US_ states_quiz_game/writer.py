from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state, x, y):
        self.teleport(x, y)
        self.write(f"{state}", align=ALIGNMENT, font=FONT)

    def winner(self):
        self.goto(0, -160)
        self.color("green")
        self.write(
            "You Completed the Quiz!", align=ALIGNMENT, font=("Courier", 20, "normal")
        )
