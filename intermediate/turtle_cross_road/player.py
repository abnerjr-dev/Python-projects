from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_dn(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.setheading(90)
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])
