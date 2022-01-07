import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

car = CarManager()
car.initial_cars()

score = Scoreboard()

game_is_on = True
count = 0
speed_car = 5

while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkeypress(player.move_up,"Up")

    for one_car in car.cars:
        one_car.move_cars()

    count += 1

    if count % 7 == 0 or count % 29 == 0:
        car.new_car(speed_car)

    for one_car in car.cars:
        if player.distance(one_car) < 25:
            score.game_over()
            game_is_on = False

    if player.cross_street():
        score.level += 1
        score.write_score()
        speed_car += 1

screen.exitonclick()
