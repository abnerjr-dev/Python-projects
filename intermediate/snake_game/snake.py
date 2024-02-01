import turtle as t

DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_piece = t.Turtle(shape="square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.teleport(position[0], position[1])
        self.snake_pieces.append(new_piece)

    def extend(self):
        self.add_segment(self.snake_pieces[-1].position())

    def move(self, snake=[]):
        snake = self.snake_pieces
        for i in range(len(snake) - 1, 0, -1):
            x = snake[i - 1].xcor()
            y = snake[i - 1].ycor()
            snake[i].goto(x, y)
        snake[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
