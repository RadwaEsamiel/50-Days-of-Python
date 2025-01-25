import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.10)
    screen.update()
    cars.extend_cars()
    score.score_update()

    if player.is_at_finish_line():
        player.goto_start()
        cars.increase_speed()
        score.level_up()


    for car in cars.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()

