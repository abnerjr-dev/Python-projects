from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1
MULTIPLIERS = [0.5, 1, 2]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(random.randrange(-300, 300, 40), random.randrange(-245, 215, 25))
        self.move_distance = STARTING_MOVE_DISTANCE

    def car_move(self):
        self.forward(self.move_distance)
        # self.forward(self.move_distance * random.choice(MULTIPLIERS))

    def car_reset(self):
        self.color(random.choice(COLORS))
        self.teleport(300, random.randrange(-245, 215, 25))

    def next_level(self):
        self.move_distance += MOVE_INCREMENT
