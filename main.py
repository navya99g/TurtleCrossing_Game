import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move,"Up")
score = Scoreboard()
cars =CarManager()
game_loop = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.at_finish_line():
        score.level_up()
        cars.level_up()

    game_loop += 1


screen.exitonclick()