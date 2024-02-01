import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("gray")
background = Background()
background.draw_border((600, 600), "black")
background.draw_assets(600, 600)


player = Player()

scoreboard = Scoreboard()

cars = []
car_amount = 30

for i in range(car_amount):
    car = CarManager()
    cars.append(car)


screen.listen()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_dn, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


game_is_on = True
refresh_timer = 0.01

while game_is_on:
    time.sleep(refresh_timer)
    screen.update()

    for c in cars:
        c.car_move()

        if c.xcor() < -300:
            c.car_reset()

        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() >= 240:
            c.next_level()

    if player.ycor() >= 240:
        player.next_level()
        scoreboard.next_level()
        refresh_timer *= 0.9


screen.exitonclick()
