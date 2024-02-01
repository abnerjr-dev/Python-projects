from turtle import Turtle

RIGHT_ANGLE = 90


class Background:
    def __init__(self):
        self.t = Turtle()

    def draw_border(self, xy_tuple, color):
        """Draws a border over x and y
        :param xy_tuple: a tuple with x and y values in pixels
        :param color: as str, "red", "blue", etc
        """
        self.t.penup()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.color(color)
        self.t.goto(-xy_tuple[0] / 2, -xy_tuple[1] / 2)
        self.t.pendown()
        for i in range(4):
            self.t.setheading(RIGHT_ANGLE * i)
            self.t.forward(xy_tuple[i % 2])

    def draw_assets(self, width, height):
        self.t.hideturtle()
        self.t.penup()
        self.t.setpos(-width / 2, -height / 2)
        self.t.pendown()
        self.t.color("white")

        # horizontal grid
        for i in range(-int(height / 2 - 66), int(height / 2 - 88), 25):
            self.t.penup()
            self.t.setpos((-width / 2 + 5, i))
            self.t.setheading(0)
            self.t.pendown()
            for _ in range(-int(width / 2), int(width / 2 - 10), 15):
                self.t.forward(10)
                self.t.penup()
                self.t.forward(5)
                self.t.pendown()

        self.t.penup()
        self.t.setpos(-width / 2, -210)

        self.t.color("grey10")
        self.t.setpos(-width / 2, height / 2 - 44)
        self.t.setheading(0)
        self.t.begin_fill()
        for i in range(4):
            self.t.setheading(RIGHT_ANGLE * i)
            self.t.forward((width, 44)[i % 2])
        self.t.end_fill()

        self.t.color("green")
        self.t.setpos(-width / 2, height / 2 - 80)
        self.t.setheading(0)
        self.t.begin_fill()
        for i in range(4):
            self.t.setheading(RIGHT_ANGLE * i)
            self.t.forward((width, 44)[i % 2])
        self.t.end_fill()

        self.t.color("green")
        self.t.setpos(-width / 2, -height / 2 - 1)
        self.t.setheading(0)
        self.t.begin_fill()
        for i in range(4):
            self.t.setheading(RIGHT_ANGLE * i)
            self.t.forward((width, 44)[i % 2])
        self.t.end_fill()

    def draw_rectangle(self, color, width, height):
        self.t.color(color)
        self.t.pendown()
        self.t.setpos(-width / 2, -height / 2)
        self.t.setheading(0)
        self.t.begin_fill()
        for i in range(4):
            self.t.setheading(RIGHT_ANGLE * i)
            self.t.forward((width, height)[i % 2])
        self.t.end_fill()
