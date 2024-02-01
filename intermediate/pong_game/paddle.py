from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.left(90)
        self.penup()
        self.color("white")
        self.shapesize(1, 5)
        self.teleport(start_pos[0], start_pos[1])

    def move_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(20)
