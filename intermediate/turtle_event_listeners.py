from turtle import Turtle, Screen

josias = Turtle()
screen = Screen()
josias.speed("fastest")


def move_forward():
    josias.forward(10)


def turn_ccw():
    josias.left(10)


def turn_cw():
    josias.right(10)


def move_backwards():
    josias.back(10)


def reset():
    josias.reset()


def pen_up():
    josias.penup()


def pen_down():
    josias.pendown()


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=turn_ccw, key="a")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_cw, key="d")
screen.onkeypress(fun=reset, key="c")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "space")


screen.exitonclick()
