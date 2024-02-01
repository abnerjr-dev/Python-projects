import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cobrinha")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    width = screen.window_width()
    height = screen.window_height()

    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.eat()

    if (
        snake.head.xcor() > int((width) / 2 - 20)
        or snake.head.xcor() < -int((width) / 2 - 20)
        or snake.head.ycor() > int((height) / 2 - 20)
        or snake.head.ycor() < -int((height) / 2 - 20)
    ):
        game_on = False
        scoreboard.game_over()

    for piece in snake.snake_pieces[1:]:
        if snake.head.distance(piece) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
