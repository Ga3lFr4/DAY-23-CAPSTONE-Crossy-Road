import random
import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager, all_cars
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#turtle_color = turtle.textinput("Color picker", "What color do you want your turtle to be?")
player = Player()
scoreboard = Scoreboard()
cars = CarManager()
cars.generate_cars()


screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in all_cars:
        car.car_move()
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.gain_level()
        player.reset_turtle()
        cars.level_up()


screen.exitonclick()