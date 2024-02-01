import turtle as t
import random as r


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8)
        self.color("red")
        self.speed(0)

        self.screen = t.Screen()
        self.width = self.screen.window_width()
        self.height = self.screen.window_height()
        self.refresh()

    def refresh(self):
        x = r.randrange(-int((self.width) / 2 - 20), int((self.width) / 2 - 20), 20)
        y = r.randrange(-int((self.height) / 2 - 20), int((self.height) / 2 - 20), 20)
        self.teleport(x, y)
