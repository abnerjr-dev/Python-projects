from turtle import Turtle
import random
import time

STARTING_DIR = [20, 45, 135, 160, -20, -45, -135, -160]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice(STARTING_DIR))

    def move(self, extra_speed):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(-(self.heading()))

        self.forward(10 + extra_speed)

    def reset(self):
        self.home()
        time.sleep(0.5)
