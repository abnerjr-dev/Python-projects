from turtle import Turtle, Screen
import random as r

josias = Turtle()
screen = Screen()
josias.shape("turtle")
josias.color("magenta", "green")
josias.speed("fastest")
screen.colormode(255)
"""
for i in range(0, 361, 1):
    josias.pencolor((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    josias.circle(100)
    josias.setheading(i)

"""

josias.pensize(15)
angles = [0, 90, 180, 360]

for i in range(200):
    josias.pencolor((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    josias.left(r.choice(angles))
    josias.forward(25)


"""
for i in range(3, 11):
    angle = 360 / i
    screen.colormode(255)
    josias.pencolor((r.randint(0, 256), r.randint(0, 256), r.randint(0, 256)))
    for s in range(i):
        josias.forward(100)
        josias.right(angle)
"""


screen.exitonclick()
