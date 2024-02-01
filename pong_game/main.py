from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right = Paddle((350, 0))
left = Paddle((-350, 0))

right_score = Scoreboard((80, 230))
left_score = Scoreboard((-80, 230))

ball = Ball()

turtle = Turtle()
turtle.pencolor("white")
turtle.hideturtle()
turtle.penup()
turtle.setheading(270)
turtle.backward(300)

for i in range(15):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

paddle_speed = 15


def tick():
    for action in keys_pressed:
        actions[action]()
    screen.update()
    # screen.ontimer(tick, frame_delay_ms)
    # frame_delay_ms = 10 default for turtle is 10 in _CFG["delay"]


actions = dict(
    ur=lambda: right.sety(right.ycor() + paddle_speed),
    dr=lambda: right.sety(right.ycor() - paddle_speed),
    ul=lambda: left.sety(left.ycor() + paddle_speed),
    dl=lambda: left.sety(left.ycor() - paddle_speed),
)

keys_pressed = set()
"""
screen.listen()

screen.onkeypress(right.move_up, "Up")
screen.onkeypress(right.move_down, "Down")
screen.onkeypress(left.move_up, "w")
screen.onkeypress(left.move_down, "s")
"""
game_on = True

extra_speed = 0

while game_on:
    # screen.update()
    time.sleep(0.05)

    screen.onkeypress(lambda: keys_pressed.add("ur"), key="Up")
    screen.onkeypress(lambda: keys_pressed.add("dr"), key="Down")
    screen.onkeyrelease(lambda: keys_pressed.remove("ur"), key="Up")
    screen.onkeyrelease(lambda: keys_pressed.remove("dr"), key="Down")
    screen.onkeypress(lambda: keys_pressed.add("ul"), key="w")
    screen.onkeypress(lambda: keys_pressed.add("dl"), key="s")
    screen.onkeyrelease(lambda: keys_pressed.remove("ul"), key="w")
    screen.onkeyrelease(lambda: keys_pressed.remove("dl"), key="s")
    screen.listen()

    ball.move(extra_speed)

    if (
        ball.xcor() > 330
        and ball.xcor() < 345
        and ball.distance(right) < 61
        or ball.xcor() < -330
        and ball.xcor() > -345
        and ball.distance(left) < 61
    ):
        ball.setheading(180 - ball.heading())
        extra_speed += 1

    if ball.xcor() > 385:
        left_score.point()
        ball.reset()
        extra_speed = 0
        ball.setheading(random.randrange(120, 220, 15))

    if ball.xcor() < -390:
        right_score.point()
        ball.reset()
        extra_speed = 0
        ball.setheading(random.randrange(-50, 50, 15))

    if right_score.score == 7 or left_score.score == 7:
        left_score.game_over()
        break

    tick()


screen.exitonclick()
